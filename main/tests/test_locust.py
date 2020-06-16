from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task(5)
    def homepage(self):
        self.client.get("/")

    @task(4)
    def getSquare1(self):
        self.client.get("/square/44")
    
    @task(4)
    def getSquare2(self):
        self.client.get("/square/33")
    
    @task(4)
    def getSquare3(self):
        self.client.get("/square/22")

    @task(4)
    def getSquare4(self):
        self.client.get("/square/11")

class User(HttpUser):
    tasks = [UserBehavior,]
    host = "http://localhost:8000"
    wait_time = between(5, 10)