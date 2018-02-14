knowrob_pepper_openease
===

Depends on the [NaoQI Python SDK](http://doc.aldebaran.com/2-5/dev/python/install_guide.html)

If you want to use basic commands like pointing and tts for pepper from openease follow this steps:

1. Start your local openEASE instance with the known start-webrob script (for further information have a look at the [openEASE documentation](http://www.knowrob.org/doc/docker))
2. Run the following command to start the server to control pepper and your local knowrob (including the ) that will be used by openEASE will , `roslaunch knowrob_pepper_openease knowrob_pepper_full.launch`
3. First log in to your local openEASE instance at [https://localhost/user/sign-in](https://localhost/user/sign-in). After this go to [https://localhost/remote](https://localhost/remote) to use the knowrob you started in step 2.
4. You can know use the predicates defined in the pepper_openease module.