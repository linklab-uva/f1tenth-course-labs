# f1tenth-course-labs
Lab Exercises and Practice Code Repo for F1/10 Autonomous Racing Course at the University of Virginia

## Instructions for how to use the code in this repo

**Step 1)**

Make sure to create a ROS workspace on your machine. Usually this can be done in the home directory.
You can do this by typing the following coommands in the terminal, one at a time.
If you already have a ROS workspace on your machine, you can skip directly to Step 2, and use your ROS workspace name instead of the name catkin_ws.

~~~bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace
cd ..
catkin_make
source ~/catkin_ws/devel/setup.bash
~~~

**Step 2)**

Next it is recommended that you create a new directory in your home folder to clone this git repository.

~~~bash
mkdir ~/github
cd ~/github
git clone https://github.com/linklab-uva/f1tenth-course-labs.git
~~~

This will create a `f1tenth-course-labs` folder inside the `github` directory you just created. 

This git repository, contains folders which are essentially ROS packages. 
For example, the repository contains a folder 'beginner_tutorials', which will contain its own subdirectories with the source code required for that package. 

**Step 3)** 

Next, you can either create a symbolic link between the package directory from the gihub folder to the package directory in the catkin_ws folder. Or you can simply copy the contents of the package to your package in the workspace folder. 

To create a symbolic link between the folder of interest, e.g. `beginner_tutorials` and the src folder in your catkin workspace, use:

~~~bash
ln -s ~/github/f1tenth-course-labs/beginner_tutorials ~/catkin_ws/src/
~~~

To copy the contents of a package from the github folder to the corresponding folder in the catkin workspace use: 

~~~bash
cp -a ~/github/f1tenth-course-labs/beginner_tutorials/. ~/catkin_ws/src/beginner_tutorials
~~~

Make sure all the python scripts are executable:
Run:

~~~bash
cd ~/catkin_ws
find . -name “*.py” -exec chmod +x {} \;
catkin_make
source ~/catkin/devel/setup.bash
~~~

Thats it !, you should now be able to run any ROS command that interacts with packages.



