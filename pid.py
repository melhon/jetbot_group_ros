from threading import currentThread
import time

class PidReg():
    def __init__(self):  
        self.Kp = 0.5
        self.Ki = 0.1
        self.Kd = 0.1

        self.P = 0.0
        self.I = 0.0
        self.D = 0.0

        # self.start_x = 0.0
        # self.goal_x = 10.0

        self.error_x = 0.0
        self.last_error_x = 0.0
        self.last_time = 0.0


    def get_vel(self, start_x, goal_x):
        self.error_x = goal_x - start_x

        self.P = self.Kp * self.error_x
        self.I = self.I + self.Ki * self.error_x
        self.D = self.Kd * ((self.error_x - self.last_error_x)/(time.time() - self.last_time))

        print("P: " + str(self.P))
        print("I: " + str(self.I))
        print("D: " + str(self.D))

        self.last_error_x = self.error_x
        self.last_time = time.time()

        return(self.P + self.I + self.D)


if __name__ == "__main__":
    reg = PidReg() 
    current_x = 0.0
    while True:
        vel = reg.get_vel(current_x, 20.0)
        current_x += vel
        print(vel)
        time.sleep(1.0)