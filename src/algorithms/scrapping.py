import sys

#to delete on real implementation (for test purpose)
authorizedNames = {"hi", "hello", "trump"}
    
#here put the scrapping algorithm
def scrap(name):
    #returns "user={name}" in case of success, "error={message}"" in case of failure
    #if user not found, message="This user doesn't seem to exist :/"
    #if scrap fails, message="Oups...Seems like Artificial Intelligence is not as intelligent as it claims to be...An error occured during the data's acquisition, please try again"
    #write scraped tweets in the file tweet.csv
    #if possible, get profile picture and write in ui/assets/user_pic.png

    if name in authorizedNames:
        return "name=" + name
    return "error=This user doesn't seem to exist :/"

print(scrap(sys.argv[1]))