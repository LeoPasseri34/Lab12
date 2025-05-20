from database.DB_connect import DBConnect
from model.arco import Arco
from model.retailer import Retailer

class DAO():

    @staticmethod
    def getCountries():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct(gr.Country) as country
                from go_retailers gr """

        cursor.execute(query)

        for row in cursor:
            result.append(row["country"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getYear():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct Year(gds.`Date`) as year
                    from go_daily_sales gds   """

        cursor.execute(query)

        for row in cursor:
            result.append(row["year"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodes(country):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from go_retailers gr 
                    where gr.Country = %s """

        cursor.execute(query, (country,))

        for row in cursor:
            result.append(Retailer(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdges(year, country):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select least(gr.Retailer_code, gr2.Retailer_code) as retailer1, 
                greatest(gr.Retailer_code, gr2.Retailer_code) as retailer2, count(distinct gds2.Product_number) as peso 
                from go_retailers gr , go_retailers gr2 , go_daily_sales gds , go_daily_sales gds2 
                where gr2.Retailer_code = gds2.Retailer_code 
                and gr.Retailer_code = gds.Retailer_code 
                and gr2.Retailer_code != gr.Retailer_code
                and year(gds2.`Date`) = year(gds.`Date`)
                and gds2.Product_number = gds.Product_number
                and gr2.Country = gr.Country
                and year(gds2.`Date`) = %s
                and gr2.Country = %s
                group by least(gr.Retailer_code, gr2.Retailer_code), greatest(gr.Retailer_code, gr2.Retailer_code)"""

        cursor.execute(query, (year, country,))

        for row in cursor:
            result.append(Arco(row['retailer1'], row['retailer2'], row['peso']))

        cursor.close()
        conn.close()
        return result
