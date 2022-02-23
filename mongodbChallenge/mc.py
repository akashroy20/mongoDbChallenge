def data_transfer(coll1):
    """This is used for creating mongodb database and transfering data to that database"""
    try:
        import logging
        from datetime import datetime
        import csv
        import pandas as pd
        d1 = datetime.now()
        a = d1.strftime("%D/%H/%M/%S").replace('/',"")
        logging.basicConfig(filename = a+'.log', level = logging.DEBUG, format = '%(asctime)s %(message)s')
        logging.info('data extraction initiated')
        
        with open('carbon_nanotubes.csv','r') as f:
            carbon_nanotubes_data = csv.reader(f, delimiter= ';')
            b = []
            for i in carbon_nanotubes_data:
                b.append(i)

            b1 = b[0]
            b2 = b[1:]

            l = []
            for i in range(1,len(b2)):
                d = {}
                for j in range(len(b1)):
                    b2[i][j] = b2[i][j].replace(',','.')
                    d[b1[j]]= float(b2[i][j])
                l.append(d)
        coll1.insert_many(l)
        logging.info('data extracted and transfered successfully')
    except Exception as e:
        logging.exception('exception occured ' + str(e))