```python
# Write your solution here
import urllib.request
import json

def retrieve_all():
    
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    my_data = (my_request.read()) # gets json data 

    data_read = json.loads(my_data)

    active_courses = []



    for course in data_read:
        if course['enabled'] == True:
            sum = 0
            for exercise in course['exercises']:
                sum += int(exercise)

            active_courses.append((course['fullName'], course['name'], course['year'], sum))


    return active_courses

def retrieve_course(course_name: str):
    courses = {} 
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses/" + course_name + "/stats")
    my_data = (my_request.read()) # gets json data 

    data_read = json.loads(my_data)


    weeks = 0
    students = 0
    hours = 0
    exercises = 0
    #data_read is the entire dictionary object, say we just want to iterate over each key, then we would do data_read.values()
    for week in data_read.values(): 
        weeks += 1

        if int((week['students'])) > students:
            students = int(week['students'])
        

        hours += int(week['hour_total'])
        exercises += int(week['exercise_total'])

    #hour_average = hours divided by students value, rounded down 
    hour_average = hours // students

    #exercises_average: the exercises value divided by the students value (rounded down to the closest integer value)
    exercises_average = exercises // students

    courses['weeks'] = weeks
    courses['students'] = students
    courses['hours'] = hours
    courses['hours_average'] = hour_average
    courses['exercises'] = exercises
    courses['exercises_average'] = exercises_average

    return courses




if __name__ == "__main__":
    print(retrieve_course("docker2019"))
```

```https://studies.cs.helsinki.fi/stats-mock/api/courses/
[{"week":7,"exercises":[17,13,13,8,6,5,11],"enabled":false,"miniproject":false,"peerReviewOpen":false,"extension":false,"_id":"59f883227655fe0034b4dfe5","year":2017,"term":"syksy","fullName":"Ohjelmistotuotanto","name":"ohtus17","url":"https://github.com/mluukkai/ohjelmistotuotanto2017/wiki/Ohjelmistotuotanto-syksy-2017","__v":7},{"week":8,"exercises":[6,14,19,22,21,21,23,23],"enabled":false,"miniproject":false,"peerReviewOpen":false,"extension":false,"_id":"5a576ac24d91600059c09180","year":1970,"term":"Unknown term","fullName":"Full stack -websovelluskehitys","name":"fs","url":"https://fullstack-hy.github.io","__v":9},{"week":8,"exercises":[6,14,19,22,21,21,23,23],"enabled":false,"miniproject":false,"peerReviewOpen":false,"extension":false,"_id":"5a7f50aa9b73740051c69898","year":2018,"term":"Unknown term","fullName":"Open Full Stack 2018","name":"ofs","url":"http://fullstackopen.github.io","__v":8},{"week":7,"exercises":[0,17,13,13,8,6,6,11],"enabled":false,"miniproject":true,"peerReviewOpen":false,"extension":false,"_id":"5bb48ca56ec4c800e33cb76f","year":2018,"term":"syksy","fullName":"Ohjelmistotuotanto","name":"ohtu2018","url":"https://github.com/mluukkai/ohjelmistotuotanto2018/wiki/Ohjelmistotuotanto-syksy-2018","__v":7},{"week":4,"exercises":[0,8,6,7,0,0,0,0],"enabled":false,"miniproject":false,"peerReviewOpen":false,"extension":false,"_id":"5be43839e90ef000b62e8ca4","year":2018,"term":"fall","fullName":"Beta DevOps with Docker","name":"docker-beta","url":"https://docker-hy.github.io","__v":3},{"week":7,"exercises":[0,11,16,16,15,15,15,15],"enabled":false,"miniproject":false,"peerReviewOpen":false,"extension":false,"_id":"5be5dfaeca8b21009ac43d35","year":2018,"term":"syksy","fullName":"Web-palvelinohjelmointi Ruby on Rails","name":"rails2018","url":"https://github.com/mluukkai/WebPalvelinohjelmointi2018","__v":7},{"week":1,"exercises":[0,9,6,7,0,0,0,0],"enabled":false,"miniproject":false,"peerReviewOpen":false,"extension":false,"_id":"5c17f2fdcccfd100f9c6a260","year":2018,"term":"christmas","fullName":"DevOps with Docker","name":"docker18","url":"https://docker-hy.github.io/","__v":3},{"week":8,"exercises":[6,14,20,22,21,21,21,20,0],"enabled":false,"miniproject":false,"peerReviewOpen":false,"extension":true,"_id":"5c39d27776e25b01007e7a12","year":2019,"term":"kevät","fullName":"Full stack websovelluskehitys","name":"fullstack2019","url":"https://fullstack-hy2019.github.io/","__v":11},{"week":8,"exercises":[0,4,4,4,5,3,3,4],"enabled":false,"miniproject":false,"peerReviewOpen":false,"extension":false,"_id":"5c3dd379e2ecb8022bb75407","year":2019,"term":"Fall","fullName":"Cloud Computing Fundamentals","name":"CCFUN","url":"https://ccfun.fi/home","__v":8},{"week":0,"exercises":[6,14,20,22,22,22,21,21,26,27],"enabled":true,"miniproject":false,"peerReviewOpen":false,"extension":true,"_id":"5c7f97d3b7e42b00495261de","year":2020,"term":"Year","fullName":"Full Stack Open 2020","name":"ofs2019","url":"https://fullstackopen.com/","__v":16},{"week":4,"exercises":[1,17,10,8,0,0,0,0],"enabled":true,"miniproject":false,"peerReviewOpen":false,"extension":false,"_id":"5cb5bcd65e4c2f005281f7e7","year":2019,"term":"Year","fullName":"DevOps with Docker 2019","name":"docker2019","url":"https://docker-hy.github.io/","__v":4},{"week":1,"exercises":[1,17,10,8],"enabled":true,"miniproject":false,"peerReviewOpen":false,"extension":false,"_id":"5e8ae0d2d9979700193caed4","name":"docker2020","url":"https://devopswithdocker.com/","term":"Year","year":2020,"fullName":"DevOps with Docker 2020","__v":0},{"week":1,"exercises":[0,13,8,7],"enabled":true,"miniproject":false,"peerReviewOpen":false,"extension":false,"_id":"5ebe6a8f54e7f10019becc15","name":"beta-dwk-20","url":"https://devopswithkubernetes.com","term":"Summer","year":2020,"fullName":"Beta DevOps with Kubernetes","__v":1}]
```