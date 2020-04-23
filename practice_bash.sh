#!/bin/zsh
set -eu
# timeout=120
# retry_delay=1
# query_with_timeout () {
# 	echo "Triggering with timeout"
# 	curl --retry $timeout --retry-connrefused --retry-delay $retry_delay 'google.com' > /dev/null
# }
# print_were_online () {
# 	echo "we're online!"
# }
# query_with_timeout && print_were_online

# name=${1}
# best_name=${2}
# # echo "Sorry $name, $best_name is my favourite."

# echo "HOME = $HOME"
# echo "DB_HOST = $DB_HOST"

# echo -n "Enter a number: "
# read var
# if [[ $var -gt 10 ]]
# then
#   echo "The variable is greater than 10."
# fi



# curl pymysql

mysql -u $DB_NAME -p$DB_PW -h $DB_HOST


#data-academy-db.cqohmuwgawul.eu-west-1.rds.amazonaws.com