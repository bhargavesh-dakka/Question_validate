import mysql.connector as sql

def create_connection():

    db = sql.connect(
        host = "localhost",
        user = "Bhargav",
        #password = "test",
        database = "question_validate"  
    )

    return db


def add_user(username, password, name):

    db = create_connection()
    cursor = db.cursor()
    try:
        cursor.execute(f"insert into users_table(username, password, name) values ('{username}','{password}','{name}');")
        db.commit()
    except:
        print("User already existed  !")
        

def validate_user(user_name, password):
    db = create_connection()
    cursor = db.cursor()

    try:
        cursor.execute(f"select username, password from users_table where username like '{user_name}'")
        details = cursor.fetchone()
        return details[0] == user_name and details[1] == password
    except:
        print("User not Found !")
        




def generate_questions():

    db = create_connection()
    cursor = db.cursor()
    cursor.execute("select * from questions;")
    answers = []
    #displaying questions and appending into list
    for i in cursor:
        print()
        print(f"{i[0]}. {i[1]}\n{i[2]}")
        print()
        while 1:
            ans = input("Enter your answer : ")
            if ans not in "abcd" or len(ans)>1:
                print("Please enter valid answer.")
            else:
                answers.append(ans)
                break
    
    cursor.close()
    db.close()
    return answers

def update_score(answers,user_name):
    db = create_connection()
    cursor = db.cursor()
    get_answers = db.cursor()
    get_answers.execute("select answer from questions")
    a = []
    for i in get_answers:
        a.append(i[0])
        
    count = 0
    for i in range(len(a)):
        if a[i] == answers[i]:
            count+=1

    cursor.execute(f"update users_table set score={count} where username like '{user_name}';")
    db.commit()
    cursor.close()
    get_answers.close()
    db.close()

    
def display_score(user_name):
    db = create_connection()
    
    total_count = db.cursor()
    total_count.execute("select count(*) from users_table")
    total_users = total_count.fetchone()[0]

    user_rank = db.cursor()
    user_rank.execute(f"with cte as(select username,dense_rank() over( order by score desc ) as ranks from users_table) select ranks from cte where username like '{user_name}';")
    print(f'You ranked {user_rank.fetchone()[0]} over {total_users} people')
    

    


    
