# CCTVFeedController

Aim: To use the raspberry pi camera as a CCTV camera which records only when motion is detected.

Imagine a scenario wherein something gets stolen from your house. With a normal security camera set up at your door, you'd have to go through hours of footage to get to the time when someone entered your house. Meanwhile, the thief could be using this precious time to cover his tracks and escape. <br />

However, with this program in place, you’d be able to easily access points where movement happened at your front door, making the process more efficient. Not only does it make reviewing feed easier, but is also easy and inexpensive to implement since it is very lightweight. It can easily be run on a raspberry pi. <br />

The program runs repeatedly and when ended, it shows the date and time of the recordings in a tabular form, using a CSV file of the format: <br />

S.No. | File Name | Start Time | Date
----- | --------- | ---------- | ----

### Classifying Feed as "Moving" or "Stationary"
This program calculates the Root Mean Squared Error (RMSE) between the RGB values of successive images clicked at 2 second intervals. If RMSE > 50, then feed is classified as "moving", else it is classified as "stationary".

Logic:
- If the camera is not recording and RMSE > 50, then recording is started
- Else if the camera is recording and RMSE < 50, then recording is stopped
- Else do nothing


## Supplies
- Raspberry Pi 3b+/4b+
- Raspberry Pi Camera Module V2
- Power Supply for Raspberry Pi
- HDMI/Micro-HDMI cable or VNC server installed on Raspberry Pi


## Physical Connections
![projectPic](https://user-images.githubusercontent.com/44669235/119965123-8c68af00-bfc7-11eb-9f3d-acabe0b2deff.jpg)
Connect the camera module to the raspberry pi's camera port.


## Raspberry Pi Setup
For this project, I installed Raspbian and the required libraries (as declared in the program) on a Raspberry Pi 4b+.

## Run the Progam
I ran the program [cctvFeedController.py](cctvFeedController.py) using Thonny.

## Output
If all goes well, your output should look like this:
### - Terminal Output <br />
![output_pic1](https://user-images.githubusercontent.com/44669235/119967758-54af3680-bfca-11eb-850e-240092c1ab19.png)
![output_pic2](https://user-images.githubusercontent.com/44669235/119967774-5842bd80-bfca-11eb-836c-4632f57fa5d7.png)

### - Video Files Created <br />
![output_pic3](https://user-images.githubusercontent.com/44669235/119967778-5973ea80-bfca-11eb-8fe2-b5e1a60beeb8.png)

### - CSV File Written <br />
![output_pic5](https://user-images.githubusercontent.com/44669235/119967786-5a0c8100-bfca-11eb-849c-b4c734c4eb7b.png)


## Social: <br />
Feel free to reach out to me in case of any queries. I'll try to reply to all questions within 24 hours.

Do share your comments. I'd love to hear about your experience while trying out the project!
1. YouTube: <br />
    a. [Scientify Inc](https://www.youtube.com/c/scientifyinc) <br />
    b. [Scientify Hindi](https://www.youtube.com/c/scientifyhindi) <br />
2. [Linkedin](https://www.linkedin.com/in/arhangoyal/) <br />
3. [Instagram](https://www.instagram.com/scientifyinc_/) <br />
4. [Instructables](https://www.instructables.com/member/Scientify%20Inc/instructables/) <br />
