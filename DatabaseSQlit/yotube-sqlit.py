import sqlite3
conn=sqlite3.connect('youtube_videos.db')
cursor=conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
 ''')

def list_videos():
    pass

def add_videos():
    pass

def update_videos():
    pass

def delete_videos():
    pass

def main():
    while True:
        print("\nYoutube Manager-SQLITE | choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        if choice=="1":
             list_videos()
        elif choice=="2":
            name=input("Enter the Video name: ")
            time=input("Enter the Video time: ")
            add_videos(name,time)
        
        elif choice=="3":
            video_id=input("Enter Video ID to Update")
            name=input("Enter the Video name: ")
            time=input("Enter the Video time: ")
            update_videos(video_id,name,time)
        
        elif choice=="4":
            video_id=input("Enter Video ID to Update")
            delete_videos(video_id)

        elif choice=="5":
            break

        else:
            print("Invalid Choice")
       



if __name__=="__main__":
    main()