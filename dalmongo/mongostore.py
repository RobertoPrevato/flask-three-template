"""
* Copyright 2015, Roberto Prevato roberto.prevato@gmail.com
* https://github.com/RobertoPrevato/Flask-three-template
*
* Licensed under the MIT license:
* http://www.opensource.org/licenses/MIT
"""
import re
from core.collections.catalogs import CatalogPage
from core.collections.listutils import ListUtils

class MongoStore():
    """
    Base class for MongoDB data providers.
    """

    def get_search_condition(self, rx, search_properties):
        return { "$or": [{ a: { "$regex": rx, "$options": "-i" } } for a in search_properties] }


    def get_catalog_page(self, collection, options):
        """
        Returns a page of results
        :param collection: db collection
        :param options: pagination options
        :return: paginated results
        """
        page_number = options["page"]
        page_size = options["size"]
        search = options["search"]
        order_by = options["orderBy"]
        sort_order = options["sortOrder"]
        skip = ((page_number-1)*page_size) if page_number > 0 else 0

        def sampling(selection, offset=0, limit=None):
            return selection[offset:(limit + offset if limit is not None else None)]

        if search is not None and search != "":
            rx = re.escape(search)
            condition = self.get_search_condition(rx, options["search_properties"])
            results = collection.find(condition)
            results = list(results)
            #obtain the total count of rows:
            total_items = len(results)

            # NB: if an order by is defined; we need to order before paginating results!
            if order_by is not None and order_by != "":
                results = ListUtils.sort_by(results, order_by, sort_order)

            #return a paginated result to the client:
            results = sampling(results, skip, page_size)
            results = [self.normalize_id(o) for o in results]

            return CatalogPage(list(results), page_number, total_items)

        total_items = collection.count()
        condition = { "$query": {}, "$orderby": {
            order_by: 1 if sort_order == "asc" else -1
        } } if order_by is not None and order_by != "" else None
        results = collection.find(condition).skip(skip).limit(page_size)

        results = [self.normalize_id(o) for o in results]
        return CatalogPage(list(results), page_number, total_items)

    @staticmethod
    def normalize_id(data):
        """
        Normalize the given object id, replacing "_id" in "id"
        The data access layer should return neutral objects, and the "_id" is a signature of MongoDB.
        """
        if data is None or not "_id" in data:
            return data
        data["id"] = str(data["_id"])
        del data["_id"]
        return data
