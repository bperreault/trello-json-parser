# modules
import os
import json

# to fill
json_file = 'clubby.json' # the json file to parse
complete_file = 'prettyjson.json'
tabdelimited_file = 'allcards_tabbed.txt'

file_extension = '.txt' # the file extension you'd like to use
end_dir = '/Users/Bobbi/GitHub/trello-json-parser' # the directory to store your cards 

# open json
with open(json_file) as data_file:
    data = json.load(data_file)

file_name = os.path.join(end_dir, complete_file)
target = open(file_name, 'a')
target.write(json.dumps(data["cards"], sort_keys=True, indent=4, separators=(',', ': '))  + "\r\n")
target.close()    
    
# variables
cards = data["cards"]
card_number = 1
total_cards = len(data["cards"])
written_cards = 0
print("Total Cards: " + str(total_cards))

complete_file = 'allcards' + file_extension
file_name = os.path.join(end_dir, complete_file)
tabdelimited_filename = os.path.join(end_dir, tabdelimited_file)

target = open(file_name, 'a')
tabdelimited = open(tabdelimited_filename, 'a')
    
tabdelimited.write("Task\tStart\tEnd\t\r\n")

# loop
for card in cards:
    print("Working on: " + card["name"])
    
    taskname = card["name"].encode('utf-8')
    target.write("\r\n - Task: " + taskname )
    tabdelimited.write( taskname + '\t')
    
    startdatejson = card["pluginData"]
    if startdatejson is not None:
        # target.write(str(startdatejson) + "\r\n - Finish Date: ")
        if len(startdatejson) > 0:
            startdate1 = str(startdatejson[0]["value"])
            startdate = json.loads(startdate1)
            
            target.write("\r\n - Starts: **** " + str(startdate["fields"]["9DF9YubN-aXHeQd"]) + " **** ")
            tabdelimited.write( str(startdate["fields"]["9DF9YubN-aXHeQd"]) + '\t')
            
        
    if card["due"] is not None:
        target.write("\r\n - Finish Date: " + card["due"] + "\r\n")
        tabdelimited.write( card["due"] + "\t\r\n")
    print("Done!")
    written_cards+=1
    card_number+=1

# message
print("======")
print(str(written_cards) + " out of " + str(total_cards) + " written successfully! :)")
target.close()
tabdelimited.close()
   