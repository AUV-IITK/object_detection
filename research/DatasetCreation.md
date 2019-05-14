# Creating dataset for images

This would be kind of a tutorial to help you walkthrough the steps that helps you get a labelled set of images, which you can use to train a Convolutional Neural Network model.

We need to feed in labelled photos (as in, a set of images, and their corresponding labels as either `txt` files or `xml` files). You would be getting rosbags for the underwater camera feeds, and you would be required to create images from them, then label it.

### 1. Gather Data

General information about a rosbag is here: [ROS BAG](http://wiki.ros.org/rosbag/Commandline)

Here, we have a rosbag named `2019-05-14-09-58-03.bag`, uploaded it in the Github repository as well. 

You can play the bag file using `rosbag play --loop <file>`.

Sometimes, the `rosbag` get corrupted, due to timing mismatches. Try to use `rosbag reindex` for fixing this.

Now, find the file rosbag2video.py. Use it accordingly to convert the given `rosbag` to a `video file`.
Link to the file: [rosbag2video](https://github.com/erlerobot/rosbag2video)

`python bag_to_video.py <bag_file>`

Apparently, bag files recorded from our current Gazebo configuration does not run correctly for the conversion.
So, I used the following hack around.

Use `rosrun image_view video_recorder` to directly record the video files.

### 2. Labelling images

For labelling the images, we'll use a commonly known repository: [LabelImg](https://github.com/tzutalin/labelImg)

There's a brilliant tutorial on how to do things on their repository `README.md` as well.
Set this up, and start labelling it in the format required, while saving the files as well.



