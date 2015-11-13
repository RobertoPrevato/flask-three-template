"""
* Copyright 2015, Roberto Prevato roberto.prevato@gmail.com
* https://github.com/RobertoPrevato/Flask-three-template
*
* Licensed under the MIT license:
* http://www.opensource.org/licenses/MIT
"""
import re
from core.collections.catalogs import CatalogPage

class MongoStore():
    """
    Base class for MongoDB data providers.
    """

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
        skip = ((page_number-1)*page_size) if page_number > 0 else 0

        def sampling(selection, offset=0, limit=None):
            return selection[offset:(limit + offset if limit is not None else None)]

        if search is not None and search != "":
            rx = re.escape(search)
            results = collection.find({ "description": { "$regex": rx, "$options": "-i" }})
            results = list(results)
            #obtain the total count of rows:
            total_items = len(results)

            #return a paginated result to the client:
            results = sampling(results, skip, page_size)
            results = [self.normalize_id(o) for o in results]

            return CatalogPage(list(results), page_number, total_items)

        total_items = collection.count()
        results = collection.find().skip(skip).limit(page_size)

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
