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
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_videos(name,time):
    cursor.execute("INSERT INTO videos(name,time) VALUES(?,?)",(name,time))
    conn.commit()


def update_videos(video_id ,new_name ,new_time):
    cursor.execute("UPDATE videosn SET name=?, time=? WHERE id=?",(new_name,new_time,video_id))
    conn.commit()


def delete_videos(video_id):
    cursor.execute("DELETE FROM videos  where id=?",(video_id,)) # tuple accept ho rha hai yaha
    conn.commit()


def main():
    while True:
        print("\nYoutube Manager-SQLITE | choose an option")
        print("1. List all youtube videos: ")
        print("2. Add a youtube video: ")
        print("3. Update a youtube video details: ")
        print("4. Delete a youtube video: ")
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


    conn.close()   



if __name__=="__main__":
    main()