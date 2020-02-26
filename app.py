from optparse import OptionParser

parser = OptionParser()
parser.add_option("--source_db", help="source database connection information ", default=None)
parser.add_option("--target_db", help="target database connection information ", default=None)
parser.add_option("--source_table", help="source table name", default=None)
parser.add_option("--target_table", help="target table name", default=None)

(options, args) = parser.parse_args()

if not options.source_db:
    raise Exception("not valid source database connection info")

if not options.source_db:
    raise Exception("not valid target database connection info")

if not options.source_db:
    raise Exception("not valid source table name")

if not options.source_db:
    raise Exception("not valid target table name")



