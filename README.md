# project
Commit-1(AKSHAR):
    - Added documentation.rtf & readme.md files for reference

Commit-2(Karan):
    #Ahiya lakh whatever you commited and sent the pull request for merging

Commit-3(Akshar):
    - pip install imutils ( do this in your machine to prevent not mpdule not found error )
    - Added out, not out buttons
    - Added function out, not_out, pending and play( #pending ),
    - CHECK IF THE FOLLOWING BUG EXISTS IN YOUR TERMINAL:
            Exception in thread Thread-2:
            Traceback (most recent call last):
            File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/threading.py", line 954, in _bootstrap_inner
                self.run()
            File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/threading.py", line 892, in run
                self._target(*self._args, **self._kwargs)
            File "/Users/aksharmehta/project/main.py", line 31, in pending
                frame = cv2.cvtColor(cv2.imread("pending.png"),cv2.COLOR_BGR2RGB) # ---> converts image to RGB   (image to be inserted.... delete the paranthesis wen done @ KARAN)
            cv2.error: OpenCV(4.5.1) /private/var/folders/nz/vv4_9tw56nv9k3tkvyszvwg80000gn/T/pip-req-build-yaf6rry6/opencv/modules/imgproc/src/color.cpp:182: error: (-215:Assertion failed) !_src.empty() in function 'cvtColor' 

To-do (Karan)
    - Add assests (welcome.png, videos etc.)
    - Try to import the video using functions.
    - Update the 4th Commit and the work done by you.
    - If any assign work for me (AKSHAR) to do in the 5th Commit