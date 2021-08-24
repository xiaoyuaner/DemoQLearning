# print(data_csv.head(3)) # Look at the first three pieces of data
# print(data_csv.info()) # View the datasheet information
# print(len(data_csv.index)) # View data volume
# print(data_csv.loc[2].values) # View the data for a specified row

# for i in range(0, data_csv.shape[0]):
#     # Read line by line        count_row = df.shape[0] # gives number of row count count_col
#     # row = data_csv.loc[i].values      take the ith data (list)
#     # print(i,'>>:',data_csv.loc[i].values) # Print the ith line data
#
#     data = data_csv.iloc[i]  # dict
#     data = (data['keyword'], data['link_detail'], data['search_num'], data['url'])
#     sql = "insert into amazon_us_link(keyword,link_detail,search_num,url) values " + str(
#         data) + ";"
#     print(sql)
#     try:
#         cur.execute(sql)  # execute sql
#         conn.commit()
#     except:
#         conn.rollback()

# cursor.execute(insert_sql, (
# str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]),
# str(row[8]), str(row[9]), str(row[10]), str(row[11]), str(row[12]), str(row[13]), str(row[14])))
# ii = i + 1


# if __name__ == '__main__':
#     path = r'F:\testProject\0906-savingCSVFilesIntoMySQL\amazon_link_0905.csv'
#     run_sql(path)


# Create table through cursor cur to operate execute() method for writing pure SQL statement.
# Then use these written sql statement in execute() method to operate data
# cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

# Insert a piece of data
# cur.execute("insert into student values('2','Tom','3 year 2 class','9')")

# update
# cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

# delete
# cur.execute("delete from student where age='9'")


# cur.execute("select * from student where age='9'")

# results = cur.fetchall()  # get the return result

# for rel in results:
#    print(rel)

# Close the Cursor
# cur.close()

# conn.commit()
# Must have conn.commit() when inserting a piece of data into the database, otherwise the data will not actually be inserted
# conn.commit()

# conn.close() close database connection
# conn.close()

# Insert multiple records at once
# sqli="insert into student values(%s,%s,%s,%s)"
# cur.executemany(sqli,[
#     ('3','Tom','1 year 1 class','6'),
#     ('3','Jack','2 year 1 class','7'),
#     ('3','Yaheng','2 year 2 class','7'),
#     ])
#
# cur.close()
# conn.commit()
# conn.close()


# if file_name_JSON == 'arrayTable':
#     data_csv.to_sql('arrayTable', engine, if_exists='replace', index=False,
#               dtype={'objId': sqlalchemy.types.BigInteger(),
#                      'key': sqlalchemy.types.String(length=20),
#                      'index': sqlalchemy.types.BigInteger(),
#                      'valStr': sqlalchemy.types.UnicodeText()
#                      })
#     with engine.connect() as con:
#         con.execute('ALTER TABLE arrayTable CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci')
#     # data_csv.to_sql(name=file_name_JSON, con=engine, if_exists='append', index=False)
#     continue


# iterate files and read line by line
# for file_name_JSON in filenames_JSON:
#     file = open(directoryLocation_JSON + '/' + file_name_JSON + '.csv',
#                 encoding='utf8mb4')
#     data_csv = pd.read_csv(file, encoding='utf8mb4')  # use pandas to read csv file
#     print(data_csv.head())
#
#     # print(data_csv.head(3)) # Look at the first three pieces of data
#     # print(data_csv.info()) # View the datasheet information
#     # print(len(data_csv.index)) # View data volume
#     # print(data_csv.loc[2].values) # View the data for a specified row
#
#     for i in range(0, data_csv.shape[0]):
#         # Read line by line        count_row = df.shape[0] # gives number of row count count_col
#         # row = data_csv.loc[i].values      take the ith data (list)
#         # print(i,'>>:',data_csv.loc[i].values) # Print the ith line data
#
#         data = data_csv.iloc[i]  # dict
#         data = (data['keyword'], data['link_detail'], data['search_num'], data['url'])
#         sql = "insert into amazon_us_link(keyword,link_detail,search_num,url) values " + str(
#             data) + ";"
#         print(sql)
#         try:
#             cur.execute(sql)  # execute sql
#             conn.commit()
#         except:
#             conn.rollback()
#
#         # cursor.execute(insert_sql, (
#         # str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]),
#         # str(row[8]), str(row[9]), str(row[10]), str(row[11]), str(row[12]), str(row[13]), str(row[14])))
#         # ii = i + 1
#
# cur.close()
# conn.close()
