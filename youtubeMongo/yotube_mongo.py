# mongodb+srv://youtubepy:<password>@atlascluster.dopnweg.mongodb.net/

from pymongo import MongoClient
from bson import ObjectId

client=MongoClient("mongodb+srv://youtubepy:<youtubepy>@atlascluster.dopnweg.mongodb.net/", tlsAllowInvalidCertificates=True)

#not good practice

db=client["ytmanager"]
video_collection=db["videos"]

#<<print(video_collection)
def list_videos():
    for video in video_collection.find():
        print(f"ID:{video['_id']},Name:{video['name']} and Time:{video['time']}")
def add_video(name,time):
    video_collection.insert_one({"name": name,"time":time})

def update_video(video_id,new_name ,new_time):
    video_collection.update_one(
        {'_id':video_id},
        {"$Set":{"name":new_name,"time":new_time}}
        )
def delete_video(video_id):
    video_collection.delete_one({"_id",video_id})

def main():
    while True:
        print("\n Youtube Manager App")
        print("1  List all videos: ")
        print("2  Add a  videos: ")
        print("3  Upadte a  videos: ")
        print("4  delete a  videos: ")
        print("5  Exit App: ")
        choice=input("Enter your Choice")
        if choice =="1":
            list_videos()
        elif choice =="2":
            name = input("Enter a Video name: ")
            time= input("Enter the time: ")
            add_video(name,time)
        elif choice =="3":

            video_id=int(input("Enter Video id"))
            name = input("Enter a Update Video name: ")
            time= input("Enter the  Updated video time: ")
            update_video(video_id,name,time)
        elif choice =="4":
            
            video_id=int(input("Enter Video id"))
            delete_video(video_id,)
        
        elif choice =="5":
            break 
        else:
            print("Invalid Choice")   
        


if __name__=="__main__":
    main()
