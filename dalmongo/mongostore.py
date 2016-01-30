"""
* Copyright 2015, Roberto Prevato roberto.prevato@gmail.com
* https://github.com/RobertoPrevato/Flask-three-template
*
* Licensed under the MIT license:
* http://www.opensource.org/licenses/MIT
"""
import re
from datetime import datetime
from core.collections.catalogs import CatalogPage
from core.collections.listutils import ListUtils

class MongoStore():
    """
    Base class for MongoDB data providers.
    """

    def get_timestamp_field(self):
        return self.options.timestamp_field if hasattr(self.options, "timestamp_field") else "timestamp"


    def get_search_condition(self, rx, search_properties, timestamp):
        or_param = [{ a: { "$regex": rx, "$options": "-i" } } for a in search_properties]
        if timestamp is not None:
            ts_field = self.get_timestamp_field()
            return {
                ts_field: { "$lt": timestamp },
                "$or": or_param
            }
        return { "$or": or_param }


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
        order_by = options["orderBy"] if "orderBy" in options else None
        sort_order = options["sortOrder"] if "sortOrder" in options else None
        timestamp = options["timestamp"] if "timestamp" in options else None
        if timestamp is not None:
            timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

        skip = ((page_number-1)*page_size) if page_number > 0 else 0

        def sampling(selection, offset=0, limit=None):
            return selection[offset:(limit + offset if limit is not None else None)]

        if search is not None and search != "":
            rx = re.escape(search)
            condition = self.get_search_condition(rx, options["search_properties"], timestamp)
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

        ts_field = self.get_timestamp_field()
        query = {} if timestamp is None else { ts_field: { "$lt": timestamp } }
        total_items = collection.count(query)
        condition = { "$query": query, "$orderby": {
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