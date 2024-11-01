text= """WEBVTT
Kind: captions
Language: en

00:00:00.060 --> 00:00:02.670 A critical flaw in IPV six has just been discovered. 00:00:02.880 --> 00:00:06.150 It affects all Windows users, so Mac and Linux, one point for you, 00:00:06.270 --> 00:00:09.750 and it allows hackers to remotely access your system without you doing anything. 00:00:09.840 --> 00:00:13.380 All hackers have to do is send a specially crafted IPV six packet to your system 00:00:14.040 --> 00:00:17.070 and they'll use an integer underflow to trigger a buffer overflow. 00:00:17.070 --> 00:00:20.280 And before you know it, you're drowning. New authentication, low complexity. 00:00:20.340 --> 00:00:24.000 It's kind of a nightmare and it's how IPV six works. That makes it even scarier. 00:00:24.060 --> 00:00:26.400 Now get your coffee ready. We're going to talk about IPV six, 00:00:26.460 --> 00:00:29.610 not because it's boring, but you just need coffee to learn. It is required. Now, 00:00:29.610 --> 00:00:32.340 IPV six, it was supposed to save the internet and it did. Now, 00:00:32.340 --> 00:00:33.690 why did it need saving? Well, 00:00:33.690 --> 00:00:35.880 because everything on the internet needs an IP address. 00:00:35.880 --> 00:00:39.150 If it wants to talk from website servers to phones to toilets, 00:00:39.330 --> 00:00:42.240 everything needs an IP address. But here's the problem. We ran out, 00:00:42.270 --> 00:00:45.450 we ran out of the IPV for addresses. You probably recognize these. 00:00:45.480 --> 00:00:49.980 They look like this or this. There were only 4.3 billion of them I know, 00:00:50.040 --> 00:00:53.250 not nearly enough. And we ran out. We dealt with that in two ways, 00:00:53.400 --> 00:00:56.520 IPV six and NAT or network address translation. 00:00:56.670 --> 00:00:59.610 Now this was cool because we could give all the devices in our home network 00:00:59.670 --> 00:01:02.850 reusable private IP addresses that are not ratable on the internet, 00:01:02.880 --> 00:01:05.820 and then give our router one unique public IPV four address. 00:01:05.940 --> 00:01:08.700 Every time any one of your devices visited something on the internet, 00:01:08.700 --> 00:01:12.450 they would use this public IP address as their IP address instead of the private 00:01:12.450 --> 00:01:15.210 one. Essentially translating it network address translation. 00:01:15.360 --> 00:01:18.810 And if something wanted to talk back, vice versa. Now this works great. 00:01:18.840 --> 00:01:21.210 It's how your house operates. It's how your business operates, 00:01:21.270 --> 00:01:24.540 and it's great for security because we have this boundary right here, 00:01:24.780 --> 00:01:28.830 this NAT translation that prevents most things from beginning into your network 00:01:28.830 --> 00:01:30.420 and accessing your devices directly. 00:01:30.480 --> 00:01:33.990 That's just the default security behavior with this. But with IPD six, 00:01:35.370 --> 00:01:36.570 it doesn't necessarily do this. 00:01:36.630 --> 00:01:39.840 And that was our other solution to running out of our 4.3 billion IPD four 00:01:39.840 --> 00:01:42.390 addresses because IPV six has this many, 00:01:42.390 --> 00:01:43.650 it's going to take me a while to write this. 00:01:48.180 --> 00:01:52.290 It has this many or 340 sillion to Killian. How do you say. 00:01:52.290 --> 00:01:53.123 That? Unci. 00:01:53.580 --> 00:01:54.360 It looks like this. 00:01:54.360 --> 00:01:56.670 And we have so many of them that we're handing them out like candy. 00:01:56.760 --> 00:02:00.510 Now this should scare you because your device probably has an IPV six address 00:02:00.750 --> 00:02:01.260 right now, 00:02:01.260 --> 00:02:04.530 and these could potentially be accessed by anyone from anywhere because they're 00:02:04.530 --> 00:02:08.220 publicly routable and may not be protected by the nat barrier like we saw with 00:02:08.220 --> 00:02:10.350 IPV four private addresses. So for example, 00:02:10.350 --> 00:02:13.350 I couldn't just connect to a device like this with this private IP address. 00:02:13.350 --> 00:02:15.150 By the way, comment below if that's your IP address. 00:02:15.210 --> 00:02:18.210 I'm actually curious to see how many people have this same IP address. 00:02:18.300 --> 00:02:21.330 Please do it. But if I were a bad news hacker up here sipping my coffee, 00:02:21.330 --> 00:02:24.810 hacking the world, there's no way for me to easily reach you directly. 00:02:24.960 --> 00:02:27.810 I would have to talk to this address which belongs to this router and it would 00:02:27.810 --> 00:02:29.880 have to agree to let me talk to you. 00:02:29.910 --> 00:02:33.180 It's like having security or a bouncer at the door. But with IPV six, 00:02:33.330 --> 00:02:37.140 your toilet might have this IPV six global Uncast address and I could connect 00:02:37.140 --> 00:02:39.600 directly to it and hack your toilet. Wouldn't that be weird? 00:02:39.720 --> 00:02:43.380 And now you're really drowning taking that joke too far. Now, 00:02:43.380 --> 00:02:45.870 how do you find out if you have an IPV six address? 00:02:45.900 --> 00:02:48.420 Let's do that right now and Windows, go ahead and launch a terminal app. 00:02:48.420 --> 00:02:50.100 Go to the search bar and type in terminal there. 00:02:50.100 --> 00:02:52.230 It's and type in one command IP config. 00:02:52.590 --> 00:02:57.090 Scroll up a bit until you find your network adapter. Mine is right here. 00:02:57.150 --> 00:03:00.550 If you have IPV six enabled, which pretty much everyone does, 00:03:00.730 --> 00:03:05.080 you'll have an address like this, an I PV six address. Here's mine. I'm done. 00:03:05.170 --> 00:03:08.770 I'm cooked. What am I going to do? Before you freak out, take a sip of coffee 00:03:11.860 --> 00:03:15.520 And know that there are different types of IPV six addresses. For example, 00:03:15.520 --> 00:03:19.780 this one right here, notice the link local part. It'll start with FE eight zero. 00:03:19.870 --> 00:03:23.800 And this is not publicly routable, right? 00:03:24.280 --> 00:03:27.460 But if you see something that starts with a two or a three, 00:03:27.670 --> 00:03:30.310 so it could be 2001 or 3001, 00:03:30.490 --> 00:03:34.480 those would be what's called A GUA Global UNCAST address. 00:03:34.540 --> 00:03:37.960 And those types of IPV six addresses are publicly routable, 00:03:38.050 --> 00:03:40.660 meaning that anyone on the internet can reach you potentially, 00:03:40.780 --> 00:03:44.260 but not in every case. There's a bit of a nuance there. We can do a test though. 00:03:44.350 --> 00:03:47.620 I've got a link below. There's a website called test ipv six.com. 00:03:47.680 --> 00:03:49.840 Really handy right now. I'll go ahead and navigate there. 00:03:49.990 --> 00:03:52.720 And this will very quickly test your IPV six connectivity. 00:03:52.780 --> 00:03:55.810 And notice right here it's seeing no IPV six address detected. 00:03:56.020 --> 00:03:58.510 Because I don't have one that I'm using to access the internet. 00:03:58.540 --> 00:04:01.840 The only one I have is Link Local that's generated by my operating system. 00:04:01.930 --> 00:04:05.800 Now this is simply because my ISP with their router is only configured to hand 00:04:05.800 --> 00:04:10.750 out IPV four addresses, but many, many ISPs are now handing out IPV six. 00:04:10.810 --> 00:04:14.020 Now, while this website does give you a good idea of your IPV six connectivity, 00:04:14.110 --> 00:04:16.210 take it with a grain of salt. I don't know your system. 00:04:16.210 --> 00:04:17.800 It could still be vulnerable. So here in a moment, 00:04:17.800 --> 00:04:20.380 we're going to break down two things. First, 00:04:20.620 --> 00:04:23.710 how is it that IPV six is hackable? What's happening? 00:04:23.770 --> 00:04:26.920 How are hackers able to actually take advantage of the T CCP IP stack? 00:04:26.950 --> 00:04:29.980 Then we'll also break down some mitigation. How do you avoid this? 00:04:30.280 --> 00:04:33.730 How do you make your system not vulnerable? That's how you say it, right? Yeah, 00:04:33.730 --> 00:04:35.890 I think so. Essentially, how do you keep yourself safe? Now, 00:04:35.890 --> 00:04:38.680 before we move on to how this hack is possible and how a hacker can take control 00:04:38.680 --> 00:04:40.000 of your computer without you even knowing, 00:04:40.300 --> 00:04:42.550 let's talk about another attack vector. Your passwords. 00:04:42.610 --> 00:04:45.790 I just read a story this morning. Let me find it real quick. Oh, right here. 00:04:45.820 --> 00:04:49.630 Hacker locks, unicorn staff out of Google accounts for four days. 00:04:49.690 --> 00:04:52.510 A hacker compromised unicorn's Google Workspace. 00:04:53.050 --> 00:04:57.700 I keep saying unicorn and changed all the passwords for all employees, 00:04:57.760 --> 00:05:00.460 locking them out of their accounts. Again, for days, 00:05:00.490 --> 00:05:03.460 that scares me because I use Google Workspace and I'm betting you, 00:05:03.790 --> 00:05:05.260 they haven't released how this happened, 00:05:05.410 --> 00:05:08.950 but I bet you someone got their password leaks somehow and it could have been 00:05:08.950 --> 00:05:11.890 any number of their employees. So what am I doing to protect myself? 00:05:11.980 --> 00:05:15.340 I use Dashlane. Dashlane is a sponsor of this video, and I'm a customer, 00:05:15.340 --> 00:05:17.440 both personal and for business. With Dashlane, 00:05:17.440 --> 00:05:20.740 I can make sure that all my employees are using unique passwords. 00:05:20.770 --> 00:05:23.500 We're also scanning the dark web to see if their passwords have been leaking to 00:05:23.500 --> 00:05:25.870 a database for any recent breaches or hacks. 00:05:25.900 --> 00:05:27.400 And I get a health score for all of them. 00:05:27.580 --> 00:05:29.980 I don't put this kind of stuff to chance. Also, 00:05:29.980 --> 00:05:32.290 I think another way this could have been avoided, I'm assuming, 00:05:32.620 --> 00:05:34.150 is using two-factor authentication. 00:05:34.360 --> 00:05:37.180 Dashlane has got built in two-factor authentication that I love because it's 00:05:37.180 --> 00:05:39.850 right here in your browser or your phone or wherever it is, 00:05:40.005 --> 00:05:43.000 because Dashlane can be installed anywhere. I love the fact that with one tool, 00:05:43.000 --> 00:05:46.030 I can put my password in and then you get my two FA code right there. 00:05:46.150 --> 00:05:49.090 I can also share that login with anyone on my team, including the two fa, 00:05:49.270 --> 00:05:50.920 which normally is a massive pain point. 00:05:51.070 --> 00:05:53.710 Do you ever get those texts when people are trying to log into your stuff that 00:05:53.710 --> 00:05:56.980 you share with them? Hey, do you have that two-factor authentication code? 00:05:57.050 --> 00:05:59.660 Did you get a text? That's so annoying, right? But Dashlane, 00:05:59.660 --> 00:06:00.530 I don't have to worry about that. 00:06:00.560 --> 00:06:02.630 They also recently implemented passkey support, 00:06:02.780 --> 00:06:05.000 which in most cases will be more secure than a password, 00:06:05.150 --> 00:06:06.470 and I've been using that anywhere I can. 00:06:06.620 --> 00:06:09.620 So let today be the day that you actually take control of your passwords, 00:06:09.680 --> 00:06:11.570 both for yourself, your family, and your business. 00:06:11.630 --> 00:06:13.670 Don't let them get hacked and don't let yourself get hacked. 00:06:13.700 --> 00:06:16.310 It's the simple stuff, the small stuff that you got to worry about. 00:06:16.310 --> 00:06:18.110 Sweat the small stuff. Take care of this right now. 00:06:18.290 --> 00:06:20.900 So check out the link of the description and use my code network check 50. 00:06:20.900 --> 00:06:22.370 You'll get 50% off at checkout. 00:06:22.550 --> 00:06:26.091 So now that we have your passwords taken care of, let's talk about IPV six. 00:06:26.091 --> 00:06:27.500 Okay, IPV six, how it's getting hacked. Now, 00:06:27.500 --> 00:06:30.200 getting to you is half the battle and that's already done. 00:06:30.200 --> 00:06:32.540 The hacker doesn't need credentials or any kind of special access. 00:06:32.570 --> 00:06:36.470 They can reach you directly. They'll start with this, an IPV six packet. 00:06:36.500 --> 00:06:40.520 They'll craft it special just for you. Baking in some hacking sauce. 00:06:40.970 --> 00:06:42.410 Is that what I'm going to call it? I don't know. 00:06:42.560 --> 00:06:46.130 This packet is specifically designed and tailored to attack your system and 00:06:46.130 --> 00:06:49.670 exploit this flaw, and they'll just start sending them a lot of them. Why not? 00:06:49.790 --> 00:06:52.610 And watch what happens when these packets arrive at the vulnerable system. 00:06:52.700 --> 00:06:53.330 Your toilet, 00:06:53.330 --> 00:06:57.110 the operating system using the T-C-P-I-P stack will start to process this 00:06:57.110 --> 00:07:00.920 packet. When it receives it, it'll come in on your ethernet cable or over wifi. 00:07:01.010 --> 00:07:04.460 And as it moves through each layer going from physical to data link to network, 00:07:04.490 --> 00:07:06.500 the operating system is essentially unwrapping it, 00:07:06.500 --> 00:07:08.630 removing layers called de encapsulation. 00:07:08.720 --> 00:07:11.600 And it's when it arrives at the network layer that things get kind of scary. 00:07:11.780 --> 00:07:12.200 And by the way, 00:07:12.200 --> 00:07:15.080 if you want to learn more about networks and the T CCP IP model and the OSI 00:07:15.080 --> 00:07:17.720 model, I've got a video somewhere around
"""

text2 = """"WEBVTT
Kind: captions
Language: en

00:00:00.000 --> 00:00:03.290 align:start position:0%
 
hey<00:00:00.599><c> there</c><00:00:00.840><c> in</c><00:00:01.380><c> this</c><00:00:01.560><c> video</c><00:00:01.740><c> we'll</c><00:00:02.460><c> create</c><00:00:02.760><c> a</c>

00:00:03.290 --> 00:00:03.300 align:start position:0%
hey there in this video we'll create a
 

00:00:03.300 --> 00:00:04.970 align:start position:0%
hey there in this video we'll create a
quick<00:00:03.480><c> and</c><00:00:03.720><c> simple</c><00:00:03.959><c> to-do</c><00:00:04.440><c> list</c><00:00:04.680><c> web</c>

00:00:04.970 --> 00:00:04.980 align:start position:0%
quick and simple to-do list web
 

00:00:04.980 --> 00:00:07.610 align:start position:0%
quick and simple to-do list web
application<00:00:05.520><c> with</c><00:00:05.819><c> the</c><00:00:05.940><c> ABP</c><00:00:06.359><c> framework</c><00:00:06.779><c> but</c>

00:00:07.610 --> 00:00:07.620 align:start position:0%
application with the ABP framework but
 

00:00:07.620 --> 00:00:09.530 align:start position:0%
application with the ABP framework but
we'll<00:00:07.859><c> be</c><00:00:08.040><c> using</c><00:00:08.400><c> the</c><00:00:08.639><c> minimalist</c><00:00:09.120><c> single</c>

00:00:09.530 --> 00:00:09.540 align:start position:0%
we'll be using the minimalist single
 

00:00:09.540 --> 00:00:11.990 align:start position:0%
we'll be using the minimalist single
layer<00:00:09.840><c> template</c><00:00:10.260><c> for</c><00:00:11.219><c> this</c><00:00:11.400><c> version</c><00:00:11.580><c> of</c><00:00:11.820><c> the</c>

00:00:11.990 --> 00:00:12.000 align:start position:0%
layer template for this version of the
 

00:00:12.000 --> 00:00:14.030 align:start position:0%
layer template for this version of the
video<00:00:12.120><c> the</c><00:00:12.900><c> UI</c><00:00:13.200><c> framework</c><00:00:13.620><c> is</c><00:00:13.799><c> going</c><00:00:13.920><c> to</c><00:00:13.980><c> be</c>

00:00:14.030 --> 00:00:14.040 align:start position:0%
video the UI framework is going to be
 

00:00:14.040 --> 00:00:16.970 align:start position:0%
video the UI framework is going to be
MVC<00:00:14.599><c> and</c><00:00:15.599><c> the</c><00:00:15.780><c> database</c><00:00:16.139><c> provider</c><00:00:16.619><c> is</c><00:00:16.800><c> going</c>

00:00:16.970 --> 00:00:16.980 align:start position:0%
MVC and the database provider is going
 

00:00:16.980 --> 00:00:18.950 align:start position:0%
MVC and the database provider is going
to<00:00:17.100><c> be</c><00:00:17.160><c> mongodb</c>

00:00:18.950 --> 00:00:18.960 align:start position:0%
to be mongodb
 

00:00:18.960 --> 00:00:20.590 align:start position:0%
to be mongodb
let's<00:00:19.440><c> get</c><00:00:19.619><c> started</c>

00:00:20.590 --> 00:00:20.600 align:start position:0%
let's get started
 

00:00:20.600 --> 00:00:23.029 align:start position:0%
let's get started
so<00:00:21.600><c> this</c><00:00:21.900><c> is</c><00:00:22.080><c> what</c><00:00:22.260><c> we're</c><00:00:22.380><c> trying</c><00:00:22.680><c> to</c><00:00:22.859><c> build</c>

00:00:23.029 --> 00:00:23.039 align:start position:0%
so this is what we're trying to build
 

00:00:23.039 --> 00:00:24.830 align:start position:0%
so this is what we're trying to build
it's<00:00:23.520><c> a</c><00:00:23.760><c> very</c><00:00:23.939><c> simple</c><00:00:24.180><c> to-do</c><00:00:24.660><c> list</c>

00:00:24.830 --> 00:00:24.840 align:start position:0%
it's a very simple to-do list
 

00:00:24.840 --> 00:00:27.290 align:start position:0%
it's a very simple to-do list
application<00:00:25.500><c> and</c><00:00:26.279><c> we</c><00:00:26.460><c> can</c><00:00:26.580><c> type</c><00:00:26.760><c> in</c><00:00:27.000><c> for</c>

00:00:27.290 --> 00:00:27.300 align:start position:0%
application and we can type in for
 

00:00:27.300 --> 00:00:30.970 align:start position:0%
application and we can type in for
example<00:00:27.740><c> feed</c><00:00:28.740><c> the</c><00:00:29.039><c> cat</c>

00:00:30.970 --> 00:00:30.980 align:start position:0%
example feed the cat
 

00:00:30.980 --> 00:00:33.770 align:start position:0%
example feed the cat
buy<00:00:31.980><c> some</c><00:00:32.279><c> milk</c>

00:00:33.770 --> 00:00:33.780 align:start position:0%
buy some milk
 

00:00:33.780 --> 00:00:36.590 align:start position:0%
buy some milk
and<00:00:34.440><c> for</c><00:00:34.680><c> example</c><00:00:34.980><c> clean</c><00:00:35.340><c> the</c><00:00:35.880><c> house</c>

00:00:36.590 --> 00:00:36.600 align:start position:0%
and for example clean the house
 

00:00:36.600 --> 00:00:38.510 align:start position:0%
and for example clean the house
so<00:00:37.079><c> we</c><00:00:37.320><c> can</c><00:00:37.440><c> type</c><00:00:37.620><c> in</c>

00:00:38.510 --> 00:00:38.520 align:start position:0%
so we can type in
 

00:00:38.520 --> 00:00:41.090 align:start position:0%
so we can type in
we<00:00:38.940><c> can</c><00:00:39.059><c> get</c><00:00:39.180><c> the</c><00:00:39.360><c> list</c><00:00:39.540><c> and</c><00:00:40.440><c> we</c><00:00:40.620><c> can</c><00:00:40.739><c> also</c>

00:00:41.090 --> 00:00:41.100 align:start position:0%
we can get the list and we can also
 

00:00:41.100 --> 00:00:43.790 align:start position:0%
we can get the list and we can also
delete

00:00:43.790 --> 00:00:43.800 align:start position:0%
 
 

00:00:43.800 --> 00:00:45.709 align:start position:0%
 
let's<00:00:44.219><c> get</c><00:00:44.399><c> started</c>

00:00:45.709 --> 00:00:45.719 align:start position:0%
let's get started
 

00:00:45.719 --> 00:00:47.330 align:start position:0%
let's get started
now<00:00:46.140><c> the</c><00:00:46.260><c> first</c><00:00:46.379><c> thing</c><00:00:46.559><c> I'll</c><00:00:46.739><c> do</c><00:00:46.980><c> is</c>

00:00:47.330 --> 00:00:47.340 align:start position:0%
now the first thing I'll do is
 

00:00:47.340 --> 00:00:49.729 align:start position:0%
now the first thing I'll do is
installing<00:00:47.820><c> the</c><00:00:48.000><c> CLI</c><00:00:48.480><c> I'm</c><00:00:49.079><c> going</c><00:00:49.200><c> to</c><00:00:49.320><c> copy</c><00:00:49.559><c> the</c>

00:00:49.729 --> 00:00:49.739 align:start position:0%
installing the CLI I'm going to copy the
 

00:00:49.739 --> 00:00:51.410 align:start position:0%
installing the CLI I'm going to copy the
install<00:00:49.920><c> command</c>

00:00:51.410 --> 00:00:51.420 align:start position:0%
install command
 

00:00:51.420 --> 00:00:53.810 align:start position:0%
install command
and<00:00:51.840><c> I'm</c><00:00:52.200><c> going</c><00:00:52.379><c> to</c><00:00:52.440><c> open</c><00:00:52.559><c> a</c><00:00:52.800><c> terminal</c>

00:00:53.810 --> 00:00:53.820 align:start position:0%
and I'm going to open a terminal
 

00:00:53.820 --> 00:00:56.090 align:start position:0%
and I'm going to open a terminal
and<00:00:54.059><c> I'll</c><00:00:54.239><c> paste</c><00:00:54.539><c> it</c><00:00:54.660><c> right</c><00:00:54.840><c> here</c>

00:00:56.090 --> 00:00:56.100 align:start position:0%
and I'll paste it right here
 

00:00:56.100 --> 00:00:57.590 align:start position:0%
and I'll paste it right here
and<00:00:56.399><c> as</c><00:00:56.640><c> you</c><00:00:56.760><c> can</c><00:00:56.820><c> see</c><00:00:56.940><c> it's</c><00:00:57.180><c> already</c><00:00:57.360><c> been</c>

00:00:57.590 --> 00:00:57.600 align:start position:0%
and as you can see it's already been
 

00:00:57.600 --> 00:00:59.630 align:start position:0%
and as you can see it's already been
installed<00:00:58.199><c> next</c><00:00:58.860><c> up</c><00:00:59.039><c> I'm</c><00:00:59.280><c> going</c><00:00:59.399><c> to</c><00:00:59.460><c> navigate</c>

00:00:59.630 --> 00:00:59.640 align:start position:0%
installed next up I'm going to navigate
 

00:00:59.640 --> 00:01:02.270 align:start position:0%
installed next up I'm going to navigate
to<00:01:00.000><c> the</c><00:01:00.180><c> desktop</c>

00:01:02.270 --> 00:01:02.280 align:start position:0%
to the desktop
 

00:01:02.280 --> 00:01:04.130 align:start position:0%
to the desktop
and<00:01:02.699><c> I'm</c><00:01:02.820><c> going</c><00:01:02.940><c> to</c><00:01:03.059><c> create</c><00:01:03.239><c> a</c><00:01:03.660><c> new</c><00:01:03.780><c> folder</c>

00:01:04.130 --> 00:01:04.140 align:start position:0%
and I'm going to create a new folder
 

00:01:04.140 --> 00:01:05.630 align:start position:0%
and I'm going to create a new folder
right<00:01:04.379><c> here</c><00:01:04.500><c> and</c><00:01:04.619><c> I'm</c><00:01:04.799><c> going</c><00:01:04.920><c> to</c><00:01:04.920><c> name</c><00:01:05.159><c> it</c><00:01:05.339><c> to</c>

00:01:05.630 --> 00:01:05.640 align:start position:0%
right here and I'm going to name it to
 

00:01:05.640 --> 00:01:09.469 align:start position:0%
right here and I'm going to name it to
do<00:01:05.820><c> app</c><00:01:06.320><c> same</c><00:01:07.320><c> name</c><00:01:07.560><c> as</c><00:01:07.920><c> our</c><00:01:08.220><c> application</c>

00:01:09.469 --> 00:01:09.479 align:start position:0%
do app same name as our application
 

00:01:09.479 --> 00:01:12.109 align:start position:0%
do app same name as our application
and<00:01:10.140><c> I'll</c><00:01:10.380><c> navigate</c><00:01:10.619><c> to</c><00:01:10.979><c> it</c>

00:01:12.109 --> 00:01:12.119 align:start position:0%
and I'll navigate to it
 

00:01:12.119 --> 00:01:14.690 align:start position:0%
and I'll navigate to it
and<00:01:12.659><c> then</c><00:01:12.720><c> I'm</c><00:01:12.840><c> gonna</c><00:01:13.020><c> copy</c><00:01:13.380><c> this</c><00:01:13.619><c> command</c><00:01:13.979><c> to</c>

00:01:14.690 --> 00:01:14.700 align:start position:0%
and then I'm gonna copy this command to
 

00:01:14.700 --> 00:01:18.109 align:start position:0%
and then I'm gonna copy this command to
create<00:01:14.880><c> the</c><00:01:15.299><c> application</c>

00:01:18.109 --> 00:01:18.119 align:start position:0%
 
 

00:01:18.119 --> 00:01:20.690 align:start position:0%
 
as<00:01:18.600><c> you</c><00:01:18.720><c> can</c><00:01:18.840><c> see</c><00:01:18.960><c> it's</c><00:01:19.320><c> a</c><00:01:19.619><c> no</c><00:01:19.920><c> layers</c><00:01:20.280><c> template</c>

00:01:20.690 --> 00:01:20.700 align:start position:0%
as you can see it's a no layers template
 

00:01:20.700 --> 00:01:22.190 align:start position:0%
as you can see it's a no layers template
which<00:01:20.939><c> is</c><00:01:21.060><c> the</c><00:01:21.240><c> minimalist</c><00:01:21.659><c> single</c><00:01:21.960><c> layer</c>

00:01:22.190 --> 00:01:22.200 align:start position:0%
which is the minimalist single layer
 

00:01:22.200 --> 00:01:24.109 align:start position:0%
which is the minimalist single layer
template<00:01:22.500><c> and</c><00:01:22.979><c> the</c><00:01:23.159><c> database</c><00:01:23.460><c> provider</c><00:01:23.939><c> is</c>

00:01:24.109 --> 00:01:24.119 align:start position:0%
template and the database provider is
 

00:01:24.119 --> 00:01:25.370 align:start position:0%
template and the database provider is
mongodb

00:01:25.370 --> 00:01:25.380 align:start position:0%
mongodb
 

00:01:25.380 --> 00:01:30.350 align:start position:0%
mongodb
and<00:01:25.920><c> the</c><00:01:26.100><c> UI</c><00:01:26.400><c> framework</c><00:01:26.820><c> is</c><00:01:27.420><c> MVC</c><00:01:28.080><c> by</c><00:01:28.320><c> default</c>

00:01:30.350 --> 00:01:30.360 align:start position:0%
and the UI framework is MVC by default
 

00:01:30.360 --> 00:01:33.950 align:start position:0%
and the UI framework is MVC by default
all<00:01:30.780><c> right</c><00:01:30.960><c> let's</c><00:01:31.380><c> open</c><00:01:31.560><c> it</c><00:01:31.860><c> up</c>

00:01:33.950 --> 00:01:33.960 align:start position:0%
all right let's open it up
 

00:01:33.960 --> 00:01:36.109 align:start position:0%
all right let's open it up
here<00:01:34.439><c> it</c><00:01:34.560><c> is</c><00:01:34.680><c> let's</c><00:01:35.100><c> run</c><00:01:35.400><c> it</c>

00:01:36.109 --> 00:01:36.119 align:start position:0%
here it is let's run it
 

00:01:36.119 --> 00:01:38.149 align:start position:0%
here it is let's run it
and<00:01:36.600><c> as</c><00:01:36.720><c> you</c><00:01:36.900><c> can</c><00:01:37.020><c> see</c><00:01:37.079><c> it's</c><00:01:37.500><c> a</c><00:01:37.680><c> minimalist</c>

00:01:38.149 --> 00:01:38.159 align:start position:0%
and as you can see it's a minimalist
 

00:01:38.159 --> 00:01:40.670 align:start position:0%
and as you can see it's a minimalist
non-layered<00:01:38.880><c> solution</c><00:01:39.299><c> and</c><00:01:39.840><c> everything</c><00:01:40.140><c> is</c>

00:01:40.670 --> 00:01:40.680 align:start position:0%
non-layered solution and everything is
 

00:01:40.680 --> 00:01:42.770 align:start position:0%
non-layered solution and everything is
in<00:01:40.920><c> one</c><00:01:41.159><c> project</c><00:01:41.520><c> we</c><00:01:42.000><c> don't</c><00:01:42.180><c> have</c><00:01:42.420><c> the</c><00:01:42.659><c> same</c>

00:01:42.770 --> 00:01:42.780 align:start position:0%
in one project we don't have the same
 

00:01:42.780 --> 00:01:45.590 align:start position:0%
in one project we don't have the same
layers<00:01:43.140><c> as</c><00:01:43.500><c> before</c><00:01:43.740><c> and</c><00:01:44.640><c> so</c><00:01:44.820><c> let's</c><00:01:45.000><c> copy</c><00:01:45.479><c> this</c>

00:01:45.590 --> 00:01:45.600 align:start position:0%
layers as before and so let's copy this
 

00:01:45.600 --> 00:01:47.630 align:start position:0%
layers as before and so let's copy this
command

00:01:47.630 --> 00:01:47.640 align:start position:0%
command
 

00:01:47.640 --> 00:01:50.030 align:start position:0%
command
and<00:01:48.240><c> let's</c><00:01:48.479><c> put</c><00:01:48.720><c> it</c><00:01:48.840><c> in</c><00:01:49.140><c> the</c><00:01:49.259><c> root</c><00:01:49.500><c> directory</c>

00:01:50.030 --> 00:01:50.040 align:start position:0%
and let's put it in the root directory
 

00:01:50.040 --> 00:01:52.249 align:start position:0%
and let's put it in the root directory
so<00:01:50.640><c> we</c><00:01:50.820><c> can</c><00:01:50.939><c> create</c><00:01:51.119><c> the</c><00:01:51.420><c> database</c><00:01:51.720><c> and</c><00:01:52.079><c> see</c>

00:01:52.249 --> 00:01:52.259 align:start position:0%
so we can create the database and see
 

00:01:52.259 --> 00:01:54.710 align:start position:0%
so we can create the database and see
the<00:01:52.439><c> initial</c><00:01:52.740><c> data</c>

00:01:54.710 --> 00:01:54.720 align:start position:0%
the initial data
 

00:01:54.720 --> 00:01:56.749 align:start position:0%
the initial data
this<00:01:55.200><c> is</c><00:01:55.259><c> the</c><00:01:55.439><c> root</c><00:01:55.560><c> directory</c>

00:01:56.749 --> 00:01:56.759 align:start position:0%
this is the root directory
 

00:01:56.759 --> 00:01:58.370 align:start position:0%
this is the root directory
and<00:01:57.060><c> I'm</c><00:01:57.299><c> going</c><00:01:57.420><c> to</c><00:01:57.420><c> open</c><00:01:57.659><c> a</c><00:01:57.899><c> command</c><00:01:58.259><c> prompt</c>

00:01:58.370 --> 00:01:58.380 align:start position:0%
and I'm going to open a command prompt
 

00:01:58.380 --> 00:01:59.870 align:start position:0%
and I'm going to open a command prompt
right<00:01:58.680><c> here</c>

00:01:59.870 --> 00:01:59.880 align:start position:0%
right here
 

00:01:59.880 --> 00:02:05.569 align:start position:0%
right here
and<00:02:00.299><c> I'll</c><00:02:00.479><c> paste</c><00:02:00.840><c> it</c><00:02:00.960><c> right</c><00:02:01.259><c> here</c>

00:02:05.569 --> 00:02:05.579 align:start position:0%
 
 

00:02:05.579 --> 00:02:08.330 align:start position:0%
 
and<00:02:06.000><c> now</c><00:02:06.180><c> we</c><00:02:06.420><c> could</c><00:02:06.600><c> run</c><00:02:06.840><c> the</c><00:02:07.560><c> project</c><00:02:07.799><c> to</c><00:02:08.160><c> see</c>

00:02:08.330 --> 00:02:08.340 align:start position:0%
and now we could run the project to see
 

00:02:08.340 --> 00:02:11.229 align:start position:0%
and now we could run the project to see
how<00:02:08.520><c> it</c><00:02:08.640><c> looks</c><00:02:08.940><c> before</c><00:02:09.119><c> we</c><00:02:09.360><c> do</c><00:02:09.539><c> anything</c>

00:02:11.229 --> 00:02:11.239 align:start position:0%
how it looks before we do anything
 

00:02:11.239 --> 00:02:14.449 align:start position:0%
how it looks before we do anything
and<00:02:12.239><c> here</c><00:02:12.420><c> is</c><00:02:12.599><c> our</c><00:02:12.900><c> singular</c><00:02:13.260><c> template</c><00:02:13.860><c> let's</c>

00:02:14.449 --> 00:02:14.459 align:start position:0%
and here is our singular template let's
 

00:02:14.459 --> 00:02:21.530 align:start position:0%
and here is our singular template let's
login

00:02:21.530 --> 00:02:21.540 align:start position:0%
 
 

00:02:21.540 --> 00:02:23.690 align:start position:0%
 
so<00:02:21.900><c> this</c><00:02:22.020><c> is</c><00:02:22.140><c> how</c><00:02:22.319><c> it</c><00:02:22.440><c> initially</c><00:02:22.800><c> looks</c><00:02:23.220><c> we</c>

00:02:23.690 --> 00:02:23.700 align:start position:0%
so this is how it initially looks we
 

00:02:23.700 --> 00:02:26.390 align:start position:0%
so this is how it initially looks we
have<00:02:23.940><c> our</c><00:02:24.300><c> UI</c><00:02:24.720><c> right</c><00:02:25.020><c> here</c><00:02:25.200><c> and</c><00:02:25.739><c> we</c><00:02:25.980><c> have</c><00:02:26.099><c> the</c>

00:02:26.390 --> 00:02:26.400 align:start position:0%
have our UI right here and we have the
 

00:02:26.400 --> 00:02:28.309 align:start position:0%
have our UI right here and we have the
administration<00:02:26.940><c> section</c><00:02:27.360><c> right</c><00:02:27.660><c> here</c><00:02:27.780><c> with</c>

00:02:28.309 --> 00:02:28.319 align:start position:0%
administration section right here with
 

00:02:28.319 --> 00:02:30.350 align:start position:0%
administration section right here with
both<00:02:28.500><c> tenant</c><00:02:29.040><c> management</c><00:02:29.220><c> and</c><00:02:29.879><c> identity</c>

00:02:30.350 --> 00:02:30.360 align:start position:0%
both tenant management and identity
 

00:02:30.360 --> 00:02:32.089 align:start position:0%
both tenant management and identity
management<00:02:30.599><c> so</c><00:02:31.260><c> for</c><00:02:31.440><c> the</c><00:02:31.620><c> tenant</c><00:02:31.920><c> management</c>

00:02:32.089 --> 00:02:32.099 align:start position:0%
management so for the tenant management
 

00:02:32.099 --> 00:02:34.490 align:start position:0%
management so for the tenant management
it<00:02:32.640><c> allows</c><00:02:32.940><c> you</c><00:02:33.060><c> to</c><00:02:33.360><c> create</c><00:02:33.599><c> a</c><00:02:34.200><c> whole</c><00:02:34.319><c> other</c>

00:02:34.490 --> 00:02:34.500 align:start position:0%
it allows you to create a whole other
 

00:02:34.500 --> 00:02:36.470 align:start position:0%
it allows you to create a whole other
tenant<00:02:35.040><c> with</c><00:02:35.340><c> its</c><00:02:35.640><c> own</c><00:02:35.700><c> identity</c><00:02:36.239><c> management</c>

00:02:36.470 --> 00:02:36.480 align:start position:0%
tenant with its own identity management
 

00:02:36.480 --> 00:02:39.470 align:start position:0%
tenant with its own identity management
for<00:02:36.900><c> both</c><00:02:37.140><c> users</c><00:02:37.680><c> and</c><00:02:37.980><c> roles</c><00:02:38.340><c> or</c><00:02:38.940><c> you</c><00:02:39.120><c> can</c><00:02:39.239><c> use</c>

00:02:39.470 --> 00:02:39.480 align:start position:0%
for both users and roles or you can use
 

00:02:39.480 --> 00:02:41.570 align:start position:0%
for both users and roles or you can use
your<00:02:39.780><c> own</c><00:02:39.900><c> roles</c><00:02:40.379><c> and</c><00:02:40.560><c> users</c><00:02:40.980><c> that</c><00:02:41.280><c> you</c><00:02:41.400><c> have</c>

00:02:41.570 --> 00:02:41.580 align:start position:0%
your own roles and users that you have
 

00:02:41.580 --> 00:02:44.270 align:start position:0%
your own roles and users that you have
in<00:02:41.940><c> your</c><00:02:42.120><c> Administration</c><00:02:42.599><c> tenant</c><00:02:43.140><c> right</c><00:02:43.319><c> here</c>

00:02:44.270 --> 00:02:44.280 align:start position:0%
in your Administration tenant right here
 

00:02:44.280 --> 00:02:47.509 align:start position:0%
in your Administration tenant right here
and<00:02:44.879><c> we</c><00:02:45.060><c> also</c><00:02:45.360><c> have</c><00:02:45.660><c> our</c><00:02:46.080><c> project</c><00:02:46.379><c> settings</c>

00:02:47.509 --> 00:02:47.519 align:start position:0%
and we also have our project settings
 

00:02:47.519 --> 00:02:49.610 align:start position:0%
and we also have our project settings
so<00:02:48.120><c> let's</c><00:02:48.300><c> stop</c><00:02:48.540><c> running</c><00:02:48.780><c> the</c><00:02:49.080><c> project</c><00:02:49.260><c> and</c>

00:02:49.610 --> 00:02:49.620 align:start position:0%
so let's stop running the project and
 

00:02:49.620 --> 00:02:52.610 align:start position:0%
so let's stop running the project and
get<00:02:49.800><c> coding</c><00:02:50.780><c> so</c><00:02:51.780><c> the</c><00:02:51.900><c> first</c><00:02:52.019><c> thing</c><00:02:52.200><c> we'll</c><00:02:52.379><c> do</c>

00:02:52.610 --> 00:02:52.620 align:start position:0%
get coding so the first thing we'll do
 

00:02:52.620 --> 00:02:54.949 align:start position:0%
get coding so the first thing we'll do
is<00:02:52.860><c> defining</c><00:02:53.340><c> the</c><00:02:53.580><c> entity</c><00:02:53.879><c> this</c><00:02:54.540><c> application</c>

00:02:54.949 --> 00:02:54.959 align:start position:0%
is defining the entity this application
 

00:02:54.959 --> 00:02:56.990 align:start position:0%
is defining the entity this application
has<00:02:55.200><c> a</c><00:02:55.379><c> single</c><00:02:55.680><c> entity</c><00:02:55.980><c> and</c><00:02:56.340><c> we'll</c><00:02:56.519><c> start</c><00:02:56.700><c> by</c>

00:02:56.990 --> 00:02:57.000 align:start position:0%
has a single entity and we'll start by
 

00:02:57.000 --> 00:02:58.850 align:start position:0%
has a single entity and we'll start by
creating<00:02:57.300><c> it</c><00:02:57.480><c> I'm</c><00:02:57.900><c> going</c><00:02:58.080><c> to</c><00:02:58.200><c> copy</c><00:02:58.440><c> this</c><00:02:58.560><c> to</c><00:02:58.739><c> do</c>

00:02:58.850 --> 00:02:58.860 align:start position:0%
creating it I'm going to copy this to do
 

00:02:58.860 --> 00:03:01.250 align:start position:0%
creating it I'm going to copy this to do
item<00:02:59.220><c> class</c><00:02:59.480><c> and</c><00:03:00.480><c> we're</c><00:03:00.599><c> going</c><00:03:00.780><c> to</c><00:03:00.900><c> create</c><00:03:01.019><c> it</c>

00:03:01.250 --> 00:03:01.260 align:start position:0%
item class and we're going to create it
 

00:03:01.260 --> 00:03:04.190 align:start position:0%
item class and we're going to create it
in<00:03:01.440><c> the</c><00:03:01.560><c> entities</c><00:03:01.800><c> folder</c><00:03:02.599><c> so</c><00:03:03.599><c> let's</c><00:03:03.780><c> find</c><00:03:04.019><c> it</c>

00:03:04.190 --> 00:03:04.200 align:start position:0%
in the entities folder so let's find it
 

00:03:04.200 --> 00:03:06.470 align:start position:0%
in the entities folder so let's find it
right<00:03:04.379><c> here</c><00:03:04.620><c> here</c><00:03:04.920><c> is</c><00:03:05.040><c> the</c><00:03:05.160><c> entities</c>

00:03:06.470 --> 00:03:06.480 align:start position:0%
right here here is the entities
 

00:03:06.480 --> 00:03:08.449 align:start position:0%
right here here is the entities
and<00:03:07.019><c> I'm</c><00:03:07.140><c> gonna</c><00:03:07.319><c> create</c><00:03:07.739><c> the</c><00:03:08.040><c> class</c><00:03:08.160><c> right</c>

00:03:08.449 --> 00:03:08.459 align:start position:0%
and I'm gonna create the class right
 

00:03:08.459 --> 00:03:11.869 align:start position:0%
and I'm gonna create the class right
here<00:03:08.700><c> to</c><00:03:09.000><c> do</c><00:03:09.120><c> hidea</c>

00:03:11.869 --> 00:03:11.879 align:start position:0%
 
 

00:03:11.879 --> 00:03:14.809 align:start position:0%
 
and<00:03:12.420><c> I'll</c><00:03:12.659><c> paste</c><00:03:13.019><c> the</c><00:03:13.080><c> code</c><00:03:13.200><c> right</c><00:03:13.500><c> here</c><00:03:14.159><c> it'll</c>

00:03:14.809 --> 00:03:14.819 align:start position:0%
and I'll paste the code right here it'll
 

00:03:14.819 --> 00:03:16.970 align:start position:0%
and I'll paste the code right here it'll
inherit<00:03:15.239><c> from</c><00:03:15.420><c> basic</c><00:03:15.720><c> aggregate</c><00:03:16.140><c> roots</c><00:03:16.440><c> in</c>

00:03:16.970 --> 00:03:16.980 align:start position:0%
inherit from basic aggregate roots in
 

00:03:16.980 --> 00:03:18.949 align:start position:0%
inherit from basic aggregate roots in
good<00:03:17.159><c> is</c><00:03:17.519><c> the</c><00:03:17.640><c> primary</c><00:03:17.940><c> key</c>

00:03:18.949 --> 00:03:18.959 align:start position:0%
good is the primary key
 

00:03:18.959 --> 00:03:20.869 align:start position:0%
good is the primary key
next<00:03:19.560><c> up</c><00:03:19.680><c> is</c><00:03:19.980><c> the</c><00:03:20.099><c> database</c><00:03:20.400><c> integration</c>

00:03:20.869 --> 00:03:20.879 align:start position:0%
next up is the database integration
 

00:03:20.879 --> 00:03:23.089 align:start position:0%
next up is the database integration
we're<00:03:21.540><c> going</c><00:03:21.720><c> to</c><00:03:21.840><c> find</c><00:03:22.019><c> the</c><00:03:22.260><c> to-do</c><00:03:22.620><c> app</c><00:03:22.680><c> DB</c>

00:03:23.089 --> 00:03:23.099 align:start position:0%
we're going to find the to-do app DB
 

00:03:23.099 --> 00:03:24.770 align:start position:0%
we're going to find the to-do app DB
context<00:03:23.459><c> class</c><00:03:23.700><c> and</c><00:03:24.239><c> we're</c><00:03:24.360><c> going</c><00:03:24.540><c> to</c><00:03:24.599><c> add</c>

00:03:24.770 --> 00:03:24.780 align:start position:0%
context class and we're going to add
 

00:03:24.780 --> 00:03:26.449 align:start position:0%
context class and we're going to add
this<00:03:25.080><c> property</c><00:03:25.440><c> to</c><00:03:25.680><c> it</c>

00:03:26.449 --> 00:03:26.459 align:start position:0%
this property to it
 

00:03:26.459 --> 00:03:28.430 align:start position:0%
this property to it
we're<00:03:26.760><c> going</c><00:03:26.940><c> to</c><00:03:27.000><c> find</c><00:03:27.120><c> the</c><00:03:27.300><c> data</c><00:03:27.599><c> folder</c>

00:03:28.430 --> 00:03:28.440 align:start position:0%
we're going to find the data folder
 

00:03:28.440 --> 00:03:30.649 align:start position:0%
we're going to find the data folder
to<00:03:28.620><c> do</c><00:03:28.800><c> apdb</c><00:03:29.340><c> context</c><00:03:29.640><c> right</c><00:03:29.879><c> here</c>

00:03:30.649 --> 00:03:30.659 align:start position:0%
to do apdb context right here
 

00:03:30.659 --> 00:03:34.190 align:start position:0%
to do apdb context right here
and<00:03:31.200><c> we</c><00:03:31.500><c> can</c><00:03:31.680><c> add</c><00:03:31.980><c> the</c><00:03:32.459><c> property</c><00:03:32.879><c> right</c><00:03:33.239><c> here</c>

00:03:34.190 --> 00:03:34.200 align:start position:0%
and we can add the property right here
 

00:03:34.200 --> 00:03:36.790 align:start position:0%
and we can add the property right here
let's<00:03:34.560><c> import</c><00:03:34.860><c> the</c><00:03:35.159><c> missing</c><00:03:35.459><c> references</c>

00:03:36.790 --> 00:03:36.800 align:start position:0%
let's import the missing references
 

00:03:36.800 --> 00:03:40.250 align:start position:0%
let's import the missing references
and<00:03:37.800><c> then</c><00:03:37.980><c> let's</c><00:03:38.220><c> copy</c><00:03:38.700><c> the</c><00:03:39.060><c> mapping</c><00:03:39.420><c> code</c><00:03:39.659><c> and</c>

00:03:40.250 --> 00:03:40.260 align:start position:0%
and then let's copy the mapping code and
 

00:03:40.260 --> 00:03:41.390 align:start position:0%
and then let's copy the mapping code and
we're<00:03:40.379><c> going</c><00:03:40.560><c> to</c><00:03:40.560><c> add</c><00:03:40.799><c> it</c><00:03:40.920><c> to</c><00:03:41.099><c> the</c><00:03:41.220><c> create</c>

00:03:41.390 --> 00:03:41.400 align:start position:0%
we're going to add it to the create
 

00:03:41.400 --> 00:03:43.850 align:start position:0%
we're going to add it to the create
model<00:03:41.819><c> method</c>

00:03:43.850 --> 00:03:43.860 align:start position:0%
model method
 

00:03:43.860 --> 00:03:46.369 align:start position:0%
model method
this<00:03:44.400><c> is</c><00:03:44.519><c> a</c><00:03:44.640><c> create</c><00:03:44.819><c> model</c><00:03:45.060><c> method</c><00:03:45.480><c> right</c><00:03:45.659><c> here</c>

00:03:46.369 --> 00:03:46.379 align:start position:0%
this is a create model method right here
 

00:03:46.379 --> 00:03:48.890 align:start position:0%
this is a create model method right here
we're<00:03:46.920><c> going</c><00:03:47.099><c> to</c><00:03:47.159><c> add</c><00:03:47.280><c> it</c><00:03:47.459><c> right</c><00:03:47.640><c> here</c><00:03:47.879><c> and</c><00:03:48.659><c> by</c>

00:03:48.890 --> 00:03:48.900 align:start position:0%
we're going to add it right here and by
 

00:03:48.900 --> 00:03:50.809 align:start position:0%
we're going to add it right here and by
that<00:03:49.080><c> we've</c><00:03:49.440><c> mapped</c><00:03:49.799><c> the</c><00:03:49.920><c> to-do</c><00:03:50.220><c> item</c><00:03:50.519><c> entity</c>

00:03:50.809 --> 00:03:50.819 align:start position:0%
that we've mapped the to-do item entity
 

00:03:50.819 --> 00:03:52.670 align:start position:0%
that we've mapped the to-do item entity
to<00:03:51.120><c> the</c><00:03:51.299><c> to</c><00:03:51.420><c> the</c><00:03:51.540><c> items</c><00:03:51.900><c> table</c><00:03:52.140><c> in</c><00:03:52.500><c> the</c>

00:03:52.670 --> 00:03:52.680 align:start position:0%
to the to the items table in the
 

00:03:52.680 --> 00:03:55.490 align:start position:0%
to the to the items table in the
database<00:03:53.519><c> next</c><00:03:54.480><c> up</c><00:03:54.659><c> is</c><00:03:54.959><c> creating</c><00:03:55.260><c> the</c>

00:03:55.490 --> 00:03:55.500 align:start position:0%
database next up is creating the
 

00:03:55.500 --> 00:03:57.410 align:start position:0%
database next up is creating the
application<00:03:55.920><c> service</c><00:03:56.220><c> an</c><00:03:57.060><c> application</c>

00:03:57.410 --> 00:03:57.420 align:start position:0%
application service an application
 

00:03:57.420 --> 00:03:59.509 align:start position:0%
application service an application
service<00:03:57.659><c> is</c><00:03:58.080><c> used</c><00:03:58.260><c> to</c><00:03:58.500><c> perform</c><00:03:58.620><c> the</c><00:03:58.980><c> use</c><00:03:59.159><c> cases</c>

00:03:59.509 --> 00:03:59.519 align:start position:0%
service is used to perform the use cases
 

00:03:59.519 --> 00:04:01.070 align:start position:0%
service is used to perform the use cases
of<00:03:59.640><c> the</c><00:03:59.760><c> application</c><00:04:00.180><c> and</c><00:04:00.659><c> we</c><00:04:00.780><c> need</c><00:04:00.900><c> to</c>

00:04:01.070 --> 00:04:01.080 align:start position:0%
of the application and we need to
 

00:04:01.080 --> 00:04:02.990 align:start position:0%
of the application and we need to
perform<00:04:01.200><c> the</c><00:04:01.620><c> following</c><00:04:01.980><c> use</c><00:04:02.220><c> cases</c><00:04:02.519><c> in</c><00:04:02.819><c> this</c>

00:04:02.990 --> 00:04:03.000 align:start position:0%
perform the following use cases in this
 

00:04:03.000 --> 00:04:04.970 align:start position:0%
perform the following use cases in this
application<00:04:03.420><c> as</c><00:04:04.019><c> we</c><00:04:04.140><c> did</c><00:04:04.260><c> in</c><00:04:04.500><c> the</c><00:04:04.620><c> example</c>

00:04:04.970 --> 00:04:04.980 align:start position:0%
application as we did in the example
 

00:04:04.980 --> 00:04:06.589 align:start position:0%
application as we did in the example
getting<00:04:05.340><c> the</c><00:04:05.580><c> list</c><00:04:05.700><c> of</c><00:04:05.879><c> these</c><00:04:06.060><c> two</c><00:04:06.180><c> items</c>

00:04:06.589 --> 00:04:06.599 align:start position:0%
getting the list of these two items
 

00:04:06.599 --> 00:04:08.750 align:start position:0%
getting the list of these two items
creating<00:04:07.140><c> a</c><00:04:07.319><c> new</c><00:04:07.500><c> to-do</c><00:04:07.799><c> item</c><00:04:08.099><c> and</c><00:04:08.340><c> deleting</c>

00:04:08.750 --> 00:04:08.760 align:start position:0%
creating a new to-do item and deleting
 

00:04:08.760 --> 00:04:10.850 align:start position:0%
creating a new to-do item and deleting
an<00:04:08.879><c> existing</c><00:04:09.239><c> to-do</c><00:04:09.599><c> item</c><00:04:09.840><c> and</c><00:04:10.500><c> so</c><00:04:10.680><c> let's</c>

00:04:10.850 --> 00:04:10.860 align:start position:0%
an existing to-do item and so let's
 

00:04:10.860 --> 00:04:13.009 align:start position:0%
an existing to-do item and so let's
create<00:04:11.099><c> the</c><00:04:11.400><c> DDO</c><00:04:11.819><c> class</c><00:04:12.000><c> before</c><00:04:12.420><c> we</c><00:04:12.780><c> start</c>

00:04:13.009 --> 00:04:13.019 align:start position:0%
create the DDO class before we start
 

00:04:13.019 --> 00:04:14.929 align:start position:0%
create the DDO class before we start
implementing<00:04:13.620><c> these</c><00:04:13.920><c> cases</c>

00:04:14.929 --> 00:04:14.939 align:start position:0%
implementing these cases
 

00:04:14.939 --> 00:04:17.390 align:start position:0%
implementing these cases
application<00:04:15.780><c> Services</c><00:04:16.079><c> typically</c><00:04:16.680><c> get</c><00:04:17.100><c> and</c>

00:04:17.390 --> 00:04:17.400 align:start position:0%
application Services typically get and
 

00:04:17.400 --> 00:04:19.849 align:start position:0%
application Services typically get and
return<00:04:17.639><c> DDOS</c><00:04:18.299><c> instead</c><00:04:18.780><c> of</c><00:04:18.900><c> entities</c><00:04:19.199><c> and</c><00:04:19.739><c> so</c>

00:04:19.849 --> 00:04:19.859 align:start position:0%
return DDOS instead of entities and so
 

00:04:19.859 --> 00:04:21.770 align:start position:0%
return DDOS instead of entities and so
let's<00:04:20.040><c> create</c><00:04:20.340><c> this</c><00:04:20.579><c> to</c><00:04:20.699><c> do</c><00:04:20.820><c> item</c><00:04:21.120><c> DDO</c><00:04:21.540><c> class</c>

00:04:21.770 --> 00:04:21.780 align:start position:0%
let's create this to do item DDO class
 

00:04:21.780 --> 00:04:23.930 align:start position:0%
let's create this to do item DDO class
under<00:04:22.199><c> the</c><00:04:22.500><c> services</c><00:04:22.680><c> folder</c><00:04:23.340><c> and</c><00:04:23.580><c> then</c><00:04:23.699><c> the</c>

00:04:23.930 --> 00:04:23.940 align:start position:0%
under the services folder and then the
 

00:04:23.940 --> 00:04:26.870 align:start position:0%
under the services folder and then the
DDOS<00:04:24.360><c> folder</c><00:04:24.840><c> I'm</c><00:04:25.380><c> going</c><00:04:25.560><c> to</c><00:04:25.620><c> copy</c><00:04:25.919><c> this</c>

00:04:26.870 --> 00:04:26.880 align:start position:0%
DDOS folder I'm going to copy this
 

00:04:26.880 --> 00:04:29.450 align:start position:0%
DDOS folder I'm going to copy this
and<00:04:27.479><c> here</c><00:04:27.600><c> is</c><00:04:27.780><c> the</c><00:04:27.900><c> services</c><00:04:28.080><c> folder</c><00:04:28.680><c> and</c><00:04:29.280><c> here</c>

00:04:29.450 --> 00:04:29.460 align:start position:0%
and here is the services folder and here
 

00:04:29.460 --> 00:04:31.790 align:start position:0%
and here is the services folder and here
is<00:04:29.580><c> the</c><00:04:29.820><c> DDOS</c><00:04:30.240><c> folder</c><00:04:31.080><c> we're</c><00:04:31.440><c> going</c><00:04:31.620><c> to</c><00:04:31.680><c> create</c>

00:04:31.790 --> 00:04:31.800 align:start position:0%
is the DDOS folder we're going to create
 

00:04:31.800 --> 00:04:33.350 align:start position:0%
is the DDOS folder we're going to create
it<00:04:31.979><c> right</c><00:04:32.160><c> here</c>

00:04:33.350 --> 00:04:33.360 align:start position:0%
it right here
 

00:04:33.360 --> 00:04:37.670 align:start position:0%
it right here
to<00:04:33.660><c> do</c><00:04:33.900><c> item</c><00:04:34.440><c> dto</c>

00:04:37.670 --> 00:04:37.680 align:start position:0%
 
 

00:04:37.680 --> 00:04:39.409 align:start position:0%
 
endless<00:04:38.280><c> Space</c><00:04:38.460><c> Center</c><00:04:38.639><c> code</c><00:04:39.000><c> right</c><00:04:39.180><c> here</c>

00:04:39.409 --> 00:04:39.419 align:start position:0%
endless Space Center code right here
 

00:04:39.419 --> 00:04:42.110 align:start position:0%
endless Space Center code right here
it's<00:04:40.259><c> a</c><00:04:40.500><c> very</c><00:04:40.680><c> simple</c><00:04:40.860><c> DDO</c><00:04:41.400><c> glass</c><00:04:41.639><c> that</c>

00:04:42.110 --> 00:04:42.120 align:start position:0%
it's a very simple DDO glass that
 

00:04:42.120 --> 00:04:44.210 align:start position:0%
it's a very simple DDO glass that
matches<00:04:42.540><c> our</c><00:04:42.720><c> entity</c><00:04:43.139><c> with</c><00:04:43.560><c> both</c><00:04:43.740><c> the</c><00:04:44.040><c> text</c>

00:04:44.210 --> 00:04:44.220 align:start position:0%
matches our entity with both the text
 

00:04:44.220 --> 00:04:45.909 align:start position:0%
matches our entity with both the text
and<00:04:45.060><c> the</c><00:04:45.240><c> good</c>

00:04:45.909 --> 00:04:45.919 align:start position:0%
and the good
 

00:04:45.919 --> 00:04:48.290 align:start position:0%
and the good
and<00:04:46.919><c> now</c><00:04:47.100><c> we're</c><00:04:47.340><c> ready</c><00:04:47.520><c> to</c><00:04:47.820><c> create</c><00:04:47.940><c> the</c>

00:04:48.290 --> 00:04:48.300 align:start position:0%
and now we're ready to create the
 

00:04:48.300 --> 00:04:50.150 align:start position:0%
and now we're ready to create the
application<00:04:48.660><c> service</c><00:04:48.960><c> class</c><00:04:49.320><c> and</c><00:04:49.800><c> implement</c>

00:04:50.150 --> 00:04:50.160 align:start position:0%
application service class and implement
 

00:04:50.160 --> 00:04:52.189 align:start position:0%
application service class and implement
it<00:04:50.400><c> and</c><00:04:50.940><c> we're</c><00:04:51.120><c> going</c><00:04:51.300><c> to</c><00:04:51.479><c> create</c><00:04:51.600><c> it</c><00:04:51.840><c> in</c><00:04:52.080><c> the</c>

00:04:52.189 --> 00:04:52.199 align:start position:0%
it and we're going to create it in the
 

00:04:52.199 --> 00:04:54.350 align:start position:0%
it and we're going to create it in the
services<00:04:52.380><c> folder</c><00:04:53.040><c> I'm</c><00:04:53.759><c> going</c><00:04:53.940><c> to</c><00:04:54.000><c> copy</c><00:04:54.240><c> it</c>

00:04:54.350 --> 00:04:54.360 align:start position:0%
services folder I'm going to copy it
 

00:04:54.360 --> 00:04:55.430 align:start position:0%
services folder I'm going to copy it
from<00:04:54.540><c> here</c>

00:04:55.430 --> 00:04:55.440 align:start position:0%
from here
 

00:04:55.440 --> 00:04:58.249 align:start position:0%
from here
and<00:04:55.919><c> here</c><00:04:56.100><c> is</c><00:04:56.280><c> the</c><00:04:56.400><c> services</c><00:04:56.520><c> folder</c>

00:04:58.249 --> 00:04:58.259 align:start position:0%
and here is the services folder
 

00:04:58.259 --> 00:05:02.629 align:start position:0%
and here is the services folder
to<00:04:58.919><c> do</c><00:04:59.100><c> app</c><00:04:59.340><c> service</c>

00:05:02.629 --> 00:05:02.639 align:start position:0%
 
 

00:05:02.639 --> 00:05:05.450 align:start position:0%
 
and<00:05:03.120><c> we'll</c><00:05:03.300><c> paste</c><00:05:03.660><c> in</c><00:05:03.720><c> the</c><00:05:03.900><c> code</c><00:05:04.080><c> right</c><00:05:04.380><c> here</c>

00:05:05.450 --> 00:05:05.460 align:start position:0%
and we'll paste in the code right here
 

00:05:05.460 --> 00:05:07.430 align:start position:0%
and we'll paste in the code right here
so<00:05:05.940><c> this</c><00:05:06.240><c> class</c><00:05:06.419><c> inherits</c><00:05:07.080><c> from</c><00:05:07.320><c> the</c>

00:05:07.430 --> 00:05:07.440 align:start position:0%
so this class inherits from the
 

00:05:07.440 --> 00:05:09.350 align:start position:0%
so this class inherits from the
application<00:05:07.800><c> service</c><00:05:08.100><c> class</c><00:05:08.520><c> which</c><00:05:09.060><c> will</c>

00:05:09.350 --> 00:05:09.360 align:start position:0%
application service class which will
 

00:05:09.360 --> 00:05:11.090 align:start position:0%
application service class which will
help<00:05:09.600><c> us</c><00:05:09.720><c> Implement</c><00:05:10.259><c> these</c><00:05:10.620><c> use</c><00:05:10.800><c> cases</c>

00:05:11.090 --> 00:05:11.100 align:start position:0%
help us Implement these use cases
 

00:05:11.100 --> 00:05:13.490 align:start position:0%
help us Implement these use cases
getting<00:05:11.639><c> them</c><00:05:11.880><c> to</c><00:05:11.940><c> do</c><00:05:12.180><c> items</c><00:05:12.540><c> deleting</c><00:05:13.440><c> a</c>

00:05:13.490 --> 00:05:13.500 align:start position:0%
getting them to do items deleting a
 

00:05:13.500 --> 00:05:16.909 align:start position:0%
getting them to do items deleting a
to-do<00:05:13.800><c> item</c><00:05:14.160><c> and</c><00:05:14.340><c> creating</c><00:05:14.639><c> a</c><00:05:14.940><c> new</c><00:05:15.000><c> to-do</c><00:05:15.479><c> item</c>

00:05:16.909 --> 00:05:16.919 align:start position:0%
to-do item and creating a new to-do item
 

00:05:16.919 --> 00:05:19.189 align:start position:0%
to-do item and creating a new to-do item
and<00:05:17.400><c> now</c><00:05:17.639><c> we're</c><00:05:17.880><c> ready</c><00:05:18.120><c> to</c><00:05:18.360><c> implement</c><00:05:18.660><c> the</c>

00:05:19.189 --> 00:05:19.199 align:start position:0%
and now we're ready to implement the
 

00:05:19.199 --> 00:05:21.830 align:start position:0%
and now we're ready to implement the
methods<00:05:19.620><c> right</c><00:05:19.860><c> here</c>

00:05:21.830 --> 00:05:21.840 align:start position:0%
methods right here
 

00:05:21.840 --> 00:05:23.629 align:start position:0%
methods right here
let's<00:05:22.320><c> start</c><00:05:22.560><c> with</c><00:05:22.860><c> the</c><00:05:22.979><c> getting</c><00:05:23.160><c> the</c><00:05:23.400><c> to-do</c>

00:05:23.629 --> 00:05:23.639 align:start position:0%
let's start with the getting the to-do
 

00:05:23.639 --> 00:05:24.890 align:start position:0%
let's start with the getting the to-do
items<00:05:24.060><c> method</c>

00:05:24.890 --> 00:05:24.900 align:start position:0%
items method
 

00:05:24.900 --> 00:05:27.170 align:start position:0%
items method
and<00:05:25.199><c> let's</c><00:05:25.440><c> paste</c><00:05:25.740><c> it</c><00:05:25.800><c> right</c><00:05:26.039><c> here</c><00:05:26.280><c> and</c><00:05:27.000><c> let's</c>

00:05:27.170 --> 00:05:27.180 align:start position:0%
and let's paste it right here and let's
 

00:05:27.180 --> 00:05:30.110 align:start position:0%
and let's paste it right here and let's
import<00:05:27.539><c> the</c><00:05:28.020><c> missing</c><00:05:28.320><c> references</c>

00:05:30.110 --> 00:05:30.120 align:start position:0%
import the missing references
 

00:05:30.120 --> 00:05:32.770 align:start position:0%
import the missing references
foreign

00:05:32.770 --> 00:05:32.780 align:start position:0%
foreign
 

00:05:32.780 --> 00:05:36.230 align:start position:0%
foreign
s<00:05:33.780><c> let's</c><00:05:34.199><c> copy</c><00:05:34.560><c> it</c><00:05:34.680><c> and</c><00:05:35.340><c> let's</c><00:05:35.639><c> paste</c><00:05:35.940><c> it</c><00:05:36.060><c> right</c>

00:05:36.230 --> 00:05:36.240 align:start position:0%
s let's copy it and let's paste it right
 

00:05:36.240 --> 00:05:39.050 align:start position:0%
s let's copy it and let's paste it right
here<00:05:36.860><c> and</c><00:05:37.860><c> finally</c><00:05:38.160><c> the</c><00:05:38.340><c> leading</c><00:05:38.639><c> a</c><00:05:38.759><c> to-do</c>

00:05:39.050 --> 00:05:39.060 align:start position:0%
here and finally the leading a to-do
 

00:05:39.060 --> 00:05:42.409 align:start position:0%
here and finally the leading a to-do
item<00:05:39.800><c> and</c><00:05:40.800><c> let's</c><00:05:41.039><c> paste</c><00:05:41.520><c> it</c><00:05:41.580><c> right</c><00:05:41.820><c> here</c><00:05:42.000><c> now</c>

00:05:42.409 --> 00:05:42.419 align:start position:0%
item and let's paste it right here now
 

00:05:42.419 --> 00:05:44.390 align:start position:0%
item and let's paste it right here now
ABP<00:05:42.960><c> provides</c><00:05:43.440><c> default</c><00:05:43.860><c> generic</c>

00:05:44.390 --> 00:05:44.400 align:start position:0%
ABP provides default generic
 

00:05:44.400 --> 00:05:46.550 align:start position:0%
ABP provides default generic
repositories<00:05:45.060><c> and</c><00:05:45.479><c> we've</c><00:05:45.780><c> used</c><00:05:45.900><c> one</c><00:05:46.199><c> right</c>

00:05:46.550 --> 00:05:46.560 align:start position:0%
repositories and we've used one right
 

00:05:46.560 --> 00:05:49.010 align:start position:0%
repositories and we've used one right
here<00:05:46.800><c> we've</c><00:05:47.520><c> injected</c><00:05:48.000><c> the</c><00:05:48.180><c> I</c><00:05:48.300><c> repository</c>

00:05:49.010 --> 00:05:49.020 align:start position:0%
here we've injected the I repository
 

00:05:49.020 --> 00:05:51.350 align:start position:0%
here we've injected the I repository
which<00:05:49.500><c> is</c><00:05:49.800><c> the</c><00:05:50.100><c> default</c><00:05:50.340><c> repository</c><00:05:51.000><c> for</c><00:05:51.240><c> the</c>

00:05:51.350 --> 00:05:51.360 align:start position:0%
which is the default repository for the
 

00:05:51.360 --> 00:05:53.270 align:start position:0%
which is the default repository for the
to<00:05:51.539><c> do</c><00:05:51.660><c> item</c><00:05:51.960><c> entity</c><00:05:52.259><c> and</c><00:05:52.680><c> then</c><00:05:52.800><c> we've</c><00:05:53.160><c> used</c>

00:05:53.270 --> 00:05:53.280 align:start position:0%
to do item entity and then we've used
 

00:05:53.280 --> 00:05:55.370 align:start position:0%
to do item entity and then we've used
its<00:05:53.759><c> methods</c><00:05:54.120><c> right</c><00:05:54.419><c> here</c>

00:05:55.370 --> 00:05:55.380 align:start position:0%
its methods right here
 

00:05:55.380 --> 00:05:57.950 align:start position:0%
its methods right here
the<00:05:55.800><c> get</c><00:05:55.979><c> list</c><00:05:56.160><c> async</c>

00:05:57.950 --> 00:05:57.960 align:start position:0%
the get list async
 

00:05:57.960 --> 00:06:00.170 align:start position:0%
the get list async
insert<00:05:58.620><c> async</c>

00:06:00.170 --> 00:06:00.180 align:start position:0%
insert async
 

00:06:00.180 --> 00:06:04.010 align:start position:0%
insert async
and<00:06:00.900><c> delete</c><00:06:01.220><c> async</c><00:06:02.460><c> these</c><00:06:03.180><c> are</c><00:06:03.300><c> all</c><00:06:03.539><c> standard</c>

00:06:04.010 --> 00:06:04.020 align:start position:0%
and delete async these are all standard
 

00:06:04.020 --> 00:06:05.990 align:start position:0%
and delete async these are all standard
repository<00:06:04.620><c> methods</c><00:06:05.100><c> to</c><00:06:05.340><c> deal</c><00:06:05.520><c> with</c><00:06:05.880><c> the</c>

00:06:05.990 --> 00:06:06.000 align:start position:0%
repository methods to deal with the
 

00:06:06.000 --> 00:06:09.110 align:start position:0%
repository methods to deal with the
database<00:06:06.560><c> and</c><00:06:07.560><c> now</c><00:06:07.800><c> we're</c><00:06:07.979><c> ready</c><00:06:08.160><c> to</c><00:06:08.460><c> code</c><00:06:08.639><c> our</c>

00:06:09.110 --> 00:06:09.120 align:start position:0%
database and now we're ready to code our
 

00:06:09.120 --> 00:06:12.310 align:start position:0%
database and now we're ready to code our
user<00:06:09.479><c> interface</c><00:06:09.900><c> let's</c><00:06:10.500><c> start</c><00:06:10.800><c> with</c><00:06:11.039><c> the</c>

00:06:12.310 --> 00:06:12.320 align:start position:0%
user interface let's start with the
 

00:06:12.320 --> 00:06:14.810 align:start position:0%
user interface let's start with the
index.cshtml.cs<00:06:13.320><c> I'll</c><00:06:13.979><c> copy</c><00:06:14.340><c> the</c><00:06:14.460><c> class</c><00:06:14.580><c> from</c>

00:06:14.810 --> 00:06:14.820 align:start position:0%
index.cshtml.cs I'll copy the class from
 

00:06:14.820 --> 00:06:15.770 align:start position:0%
index.cshtml.cs I'll copy the class from
here

00:06:15.770 --> 00:06:15.780 align:start position:0%
here
 

00:06:15.780 --> 00:06:20.210 align:start position:0%
here
and<00:06:16.500><c> I'm</c><00:06:16.740><c> gonna</c><00:06:16.979><c> find</c><00:06:17.280><c> it</c><00:06:17.600><c> right</c><00:06:18.600><c> here</c>

00:06:20.210 --> 00:06:20.220 align:start position:0%
and I'm gonna find it right here
 

00:06:20.220 --> 00:06:22.430 align:start position:0%
and I'm gonna find it right here
and<00:06:20.639><c> I'll</c><00:06:20.820><c> paste</c><00:06:21.180><c> it</c><00:06:21.300><c> right</c><00:06:21.539><c> here</c>

00:06:22.430 --> 00:06:22.440 align:start position:0%
and I'll paste it right here
 

00:06:22.440 --> 00:06:24.710 align:start position:0%
and I'll paste it right here
now<00:06:22.979><c> this</c><00:06:23.340><c> class</c><00:06:23.520><c> uses</c><00:06:24.060><c> the</c><00:06:24.240><c> to-do</c><00:06:24.539><c> app</c>

00:06:24.710 --> 00:06:24.720 align:start position:0%
now this class uses the to-do app
 

00:06:24.720 --> 00:06:26.390 align:start position:0%
now this class uses the to-do app
service<00:06:24.960><c> to</c><00:06:25.319><c> get</c><00:06:25.440><c> the</c><00:06:25.620><c> list</c><00:06:25.740><c> of</c><00:06:25.979><c> the</c><00:06:26.100><c> to-do</c>

00:06:26.390 --> 00:06:26.400 align:start position:0%
service to get the list of the to-do
 

00:06:26.400 --> 00:06:28.249 align:start position:0%
service to get the list of the to-do
items<00:06:26.759><c> and</c><00:06:27.060><c> assign</c><00:06:27.419><c> the</c><00:06:27.539><c> to-do</c><00:06:27.900><c> items</c>

00:06:28.249 --> 00:06:28.259 align:start position:0%
items and assign the to-do items
 

00:06:28.259 --> 00:06:30.469 align:start position:0%
items and assign the to-do items
property<00:06:28.680><c> and</c><00:06:29.280><c> we'll</c><00:06:29.460><c> use</c><00:06:29.639><c> it</c><00:06:29.880><c> to</c><00:06:30.060><c> render</c><00:06:30.240><c> the</c>

00:06:30.469 --> 00:06:30.479 align:start position:0%
property and we'll use it to render the
 

00:06:30.479 --> 00:06:33.170 align:start position:0%
property and we'll use it to render the
to-do<00:06:30.840><c> items</c><00:06:31.139><c> on</c><00:06:31.440><c> the</c><00:06:31.560><c> Razer</c><00:06:31.860><c> page</c>

00:06:33.170 --> 00:06:33.180 align:start position:0%
to-do items on the Razer page
 

00:06:33.180 --> 00:06:38.210 align:start position:0%
to-do items on the Razer page
next<00:06:33.900><c> up</c><00:06:34.080><c> let's</c><00:06:34.380><c> copy</c><00:06:34.740><c> the</c><00:06:34.919><c> index.cshtml</c>

00:06:38.210 --> 00:06:38.220 align:start position:0%
 
 

00:06:38.220 --> 00:06:39.650 align:start position:0%
 
and

00:06:39.650 --> 00:06:39.660 align:start position:0%
and
 

00:06:39.660 --> 00:06:41.809 align:start position:0%
and
we'll<00:06:40.139><c> space</c><00:06:40.440><c> it</c><00:06:40.680><c> right</c><00:06:40.979><c> here</c>

00:06:41.809 --> 00:06:41.819 align:start position:0%
we'll space it right here
 

00:06:41.819 --> 00:06:44.689 align:start position:0%
we'll space it right here
we're<00:06:42.360><c> using</c><00:06:42.720><c> ABP</c><00:06:43.199><c> card</c><00:06:43.440><c> tag</c><00:06:43.860><c> helpers</c><00:06:44.280><c> to</c><00:06:44.580><c> make</c>

00:06:44.689 --> 00:06:44.699 align:start position:0%
we're using ABP card tag helpers to make
 

00:06:44.699 --> 00:06:47.090 align:start position:0%
we're using ABP card tag helpers to make
a<00:06:44.940><c> simple</c><00:06:45.060><c> card</c><00:06:45.360><c> view</c><00:06:45.660><c> you</c><00:06:46.440><c> could</c><00:06:46.560><c> still</c><00:06:46.800><c> use</c>

00:06:47.090 --> 00:06:47.100 align:start position:0%
a simple card view you could still use
 

00:06:47.100 --> 00:06:49.610 align:start position:0%
a simple card view you could still use
the<00:06:47.460><c> standard</c><00:06:47.699><c> bootstrap</c><00:06:48.360><c> in</c><00:06:48.539><c> HTML</c><00:06:49.199><c> structure</c>

00:06:49.610 --> 00:06:49.620 align:start position:0%
the standard bootstrap in HTML structure
 

00:06:49.620 --> 00:06:52.010 align:start position:0%
the standard bootstrap in HTML structure
however<00:06:50.160><c> ABP</c><00:06:50.759><c> tag</c><00:06:51.000><c> helpers</c><00:06:51.419><c> make</c><00:06:51.660><c> it</c><00:06:51.840><c> much</c>

00:06:52.010 --> 00:06:52.020 align:start position:0%
however ABP tag helpers make it much
 

00:06:52.020 --> 00:06:54.590 align:start position:0%
however ABP tag helpers make it much
easier<00:06:52.440><c> and</c><00:06:52.620><c> safer</c><00:06:53.039><c> and</c><00:06:53.759><c> we</c><00:06:53.940><c> also</c><00:06:54.180><c> have</c><00:06:54.360><c> some</c>

00:06:54.590 --> 00:06:54.600 align:start position:0%
easier and safer and we also have some
 

00:06:54.600 --> 00:06:56.570 align:start position:0%
easier and safer and we also have some
scripts<00:06:54.960><c> and</c><00:06:55.080><c> styles</c><00:06:55.500><c> right</c><00:06:55.680><c> here</c><00:06:55.860><c> so</c><00:06:56.160><c> let's</c>

00:06:56.570 --> 00:06:56.580 align:start position:0%
scripts and styles right here so let's
 

00:06:56.580 --> 00:06:59.029 align:start position:0%
scripts and styles right here so let's
Implement<00:06:57.000><c> them</c>

00:06:59.029 --> 00:06:59.039 align:start position:0%
Implement them
 

00:06:59.039 --> 00:07:01.450 align:start position:0%
Implement them
let's<00:06:59.460><c> copy</c><00:06:59.819><c> the</c><00:06:59.940><c> JavaScript</c><00:07:00.360><c> code</c>

00:07:01.450 --> 00:07:01.460 align:start position:0%
let's copy the JavaScript code
 

00:07:01.460 --> 00:07:05.029 align:start position:0%
let's copy the JavaScript code
and<00:07:02.460><c> let's</c><00:07:02.699><c> create</c><00:07:03.000><c> the</c><00:07:03.600><c> JavaScript</c><00:07:04.080><c> file</c>

00:07:05.029 --> 00:07:05.039 align:start position:0%
and let's create the JavaScript file
 

00:07:05.039 --> 00:07:06.409 align:start position:0%
and let's create the JavaScript file
right<00:07:05.400><c> here</c>

00:07:06.409 --> 00:07:06.419 align:start position:0%
right here
 

00:07:06.419 --> 00:07:11.570 align:start position:0%
right here
index<00:07:07.759><c> dot</c><00:07:08.759><c> CS</c><00:07:09.120><c> HTML</c>

00:07:11.570 --> 00:07:11.580 align:start position:0%
index dot CS HTML
 

00:07:11.580 --> 00:07:14.090 align:start position:0%
index dot CS HTML
and<00:07:12.000><c> let's</c><00:07:12.240><c> paste</c><00:07:12.600><c> it</c><00:07:12.660><c> right</c><00:07:12.840><c> here</c>

00:07:14.090 --> 00:07:14.100 align:start position:0%
and let's paste it right here
 

00:07:14.100 --> 00:07:16.430 align:start position:0%
and let's paste it right here
so<00:07:14.580><c> for</c><00:07:14.699><c> the</c><00:07:14.880><c> first</c><00:07:15.060><c> part</c><00:07:15.300><c> of</c><00:07:15.479><c> the</c><00:07:15.600><c> code</c><00:07:15.780><c> we've</c>

00:07:16.430 --> 00:07:16.440 align:start position:0%
so for the first part of the code we've
 

00:07:16.440 --> 00:07:18.350 align:start position:0%
so for the first part of the code we've
registered<00:07:16.919><c> to</c><00:07:17.100><c> The</c><00:07:17.280><c> Click</c><00:07:17.580><c> event</c><00:07:17.759><c> on</c><00:07:18.180><c> the</c>

00:07:18.350 --> 00:07:18.360 align:start position:0%
registered to The Click event on the
 

00:07:18.360 --> 00:07:20.870 align:start position:0%
registered to The Click event on the
trash<00:07:18.539><c> icon</c><00:07:19.020><c> near</c><00:07:19.319><c> the</c><00:07:19.500><c> to</c><00:07:19.620><c> do</c><00:07:19.740><c> items</c><00:07:20.160><c> we've</c>

00:07:20.870 --> 00:07:20.880 align:start position:0%
trash icon near the to do items we've
 

00:07:20.880 --> 00:07:22.670 align:start position:0%
trash icon near the to do items we've
deleted<00:07:21.180><c> the</c><00:07:21.360><c> related</c><00:07:21.660><c> to</c><00:07:21.840><c> do</c><00:07:21.960><c> item</c><00:07:22.319><c> on</c><00:07:22.500><c> the</c>

00:07:22.670 --> 00:07:22.680 align:start position:0%
deleted the related to do item on the
 

00:07:22.680 --> 00:07:24.890 align:start position:0%
deleted the related to do item on the
server<00:07:22.979><c> and</c><00:07:23.400><c> showed</c><00:07:23.759><c> a</c><00:07:23.940><c> notification</c><00:07:24.419><c> on</c><00:07:24.720><c> the</c>

00:07:24.890 --> 00:07:24.900 align:start position:0%
server and showed a notification on the
 

00:07:24.900 --> 00:07:27.110 align:start position:0%
server and showed a notification on the
UI<00:07:25.199><c> which</c><00:07:25.620><c> says</c><00:07:25.979><c> that</c><00:07:26.160><c> these</c><00:07:26.520><c> two</c><00:07:26.699><c> item</c><00:07:27.000><c> has</c>

00:07:27.110 --> 00:07:27.120 align:start position:0%
UI which says that these two item has
 

00:07:27.120 --> 00:07:29.150 align:start position:0%
UI which says that these two item has
been<00:07:27.240><c> deleted</c><00:07:27.660><c> right</c><00:07:28.020><c> and</c><00:07:28.620><c> we've</c><00:07:28.860><c> also</c>

00:07:29.150 --> 00:07:29.160 align:start position:0%
been deleted right and we've also
 

00:07:29.160 --> 00:07:31.249 align:start position:0%
been deleted right and we've also
removed<00:07:29.520><c> it</c><00:07:29.639><c> from</c><00:07:29.940><c> the</c><00:07:30.060><c> Dom</c><00:07:30.240><c> so</c><00:07:30.900><c> we</c><00:07:31.080><c> wouldn't</c>

00:07:31.249 --> 00:07:31.259 align:start position:0%
removed it from the Dom so we wouldn't
 

00:07:31.259 --> 00:07:33.589 align:start position:0%
removed it from the Dom so we wouldn't
need<00:07:31.500><c> to</c><00:07:31.680><c> refresh</c><00:07:32.039><c> the</c><00:07:32.220><c> page</c><00:07:32.520><c> every</c><00:07:32.940><c> time</c><00:07:33.240><c> we</c>

00:07:33.589 --> 00:07:33.599 align:start position:0%
need to refresh the page every time we
 

00:07:33.599 --> 00:07:35.809 align:start position:0%
need to refresh the page every time we
delete<00:07:33.780><c> something</c><00:07:34.199><c> and</c><00:07:35.039><c> on</c><00:07:35.220><c> the</c><00:07:35.340><c> second</c><00:07:35.520><c> part</c>

00:07:35.809 --> 00:07:35.819 align:start position:0%
delete something and on the second part
 

00:07:35.819 --> 00:07:38.210 align:start position:0%
delete something and on the second part
we've<00:07:36.300><c> created</c><00:07:36.599><c> a</c><00:07:36.960><c> new</c><00:07:37.080><c> to-do</c><00:07:37.500><c> item</c><00:07:37.800><c> on</c><00:07:38.039><c> the</c>

00:07:38.210 --> 00:07:38.220 align:start position:0%
we've created a new to-do item on the
 

00:07:38.220 --> 00:07:40.730 align:start position:0%
we've created a new to-do item on the
server<00:07:38.580><c> and</c><00:07:39.120><c> if</c><00:07:39.360><c> it</c><00:07:39.539><c> succeeded</c><00:07:40.020><c> we</c><00:07:40.380><c> would</c><00:07:40.560><c> then</c>

00:07:40.730 --> 00:07:40.740 align:start position:0%
server and if it succeeded we would then
 

00:07:40.740 --> 00:07:43.790 align:start position:0%
server and if it succeeded we would then
manipulate<00:07:41.340><c> the</c><00:07:41.520><c> Dom</c><00:07:41.759><c> to</c><00:07:42.660><c> insert</c><00:07:43.020><c> a</c><00:07:43.380><c> new</c><00:07:43.560><c> list</c>

00:07:43.790 --> 00:07:43.800 align:start position:0%
manipulate the Dom to insert a new list
 

00:07:43.800 --> 00:07:46.129 align:start position:0%
manipulate the Dom to insert a new list
item<00:07:44.220><c> element</c><00:07:44.400><c> to</c><00:07:44.819><c> the</c><00:07:45.000><c> to-do</c><00:07:45.300><c> list</c><00:07:45.419><c> in</c><00:07:45.960><c> this</c>

00:07:46.129 --> 00:07:46.139 align:start position:0%
item element to the to-do list in this
 

00:07:46.139 --> 00:07:48.110 align:start position:0%
item element to the to-do list in this
way<00:07:46.319><c> we</c><00:07:46.680><c> wouldn't</c><00:07:46.860><c> need</c><00:07:47.160><c> to</c><00:07:47.280><c> refresh</c><00:07:47.639><c> the</c><00:07:47.819><c> page</c>

00:07:48.110 --> 00:07:48.120 align:start position:0%
way we wouldn't need to refresh the page
 

00:07:48.120 --> 00:07:51.010 align:start position:0%
way we wouldn't need to refresh the page
every<00:07:48.539><c> time</c><00:07:48.900><c> we</c><00:07:49.319><c> create</c><00:07:49.560><c> a</c><00:07:49.979><c> new</c><00:07:50.099><c> to-do</c><00:07:50.520><c> item</c>

00:07:51.010 --> 00:07:51.020 align:start position:0%
every time we create a new to-do item
 

00:07:51.020 --> 00:07:54.469 align:start position:0%
every time we create a new to-do item
and<00:07:52.020><c> last</c><00:07:52.199><c> but</c><00:07:52.380><c> not</c><00:07:52.560><c> least</c><00:07:52.800><c> the</c><00:07:53.220><c> CSS</c><00:07:53.699><c> let's</c>

00:07:54.469 --> 00:07:54.479 align:start position:0%
and last but not least the CSS let's
 

00:07:54.479 --> 00:07:56.809 align:start position:0%
and last but not least the CSS let's
copy<00:07:54.840><c> the</c><00:07:54.960><c> code</c>

00:07:56.809 --> 00:07:56.819 align:start position:0%
copy the code
 

00:07:56.819 --> 00:07:59.749 align:start position:0%
copy the code
and<00:07:57.479><c> let's</c><00:07:57.720><c> add</c><00:07:57.960><c> it</c><00:07:58.139><c> right</c><00:07:58.380><c> here</c><00:07:58.680><c> and</c><00:07:59.340><c> by</c><00:07:59.520><c> that</c>

00:07:59.749 --> 00:07:59.759 align:start position:0%
and let's add it right here and by that
 

00:07:59.759 --> 00:08:03.469 align:start position:0%
and let's add it right here and by that
we<00:08:00.120><c> can</c><00:08:00.240><c> run</c><00:08:00.539><c> the</c><00:08:00.960><c> project</c>

00:08:03.469 --> 00:08:03.479 align:start position:0%
 
 

00:08:03.479 --> 00:08:05.930 align:start position:0%
 
and<00:08:04.020><c> here</c><00:08:04.259><c> is</c><00:08:04.440><c> our</c><00:08:04.979><c> little</c><00:08:05.280><c> minimalist</c>

00:08:05.930 --> 00:08:05.940 align:start position:0%
and here is our little minimalist
 

00:08:05.940 --> 00:08:08.570 align:start position:0%
and here is our little minimalist
application<00:08:06.539><c> of</c><00:08:06.780><c> the</c><00:08:06.900><c> to-do</c><00:08:07.199><c> list</c><00:08:07.380><c> let's</c><00:08:08.280><c> add</c>

00:08:08.570 --> 00:08:08.580 align:start position:0%
application of the to-do list let's add
 

00:08:08.580 --> 00:08:12.170 align:start position:0%
application of the to-do list let's add
something<00:08:08.819><c> let's</c><00:08:09.240><c> say</c><00:08:09.479><c> to</c><00:08:09.780><c> do</c><00:08:10.020><c> item</c>

00:08:12.170 --> 00:08:12.180 align:start position:0%
something let's say to do item
 

00:08:12.180 --> 00:08:13.610 align:start position:0%
something let's say to do item
one

00:08:13.610 --> 00:08:13.620 align:start position:0%
one
 

00:08:13.620 --> 00:08:17.510 align:start position:0%
one
to<00:08:13.740><c> do</c><00:08:14.160><c> wirem</c><00:08:14.880><c> two</c><00:08:15.479><c> and</c><00:08:16.259><c> three</c><00:08:16.500><c> so</c><00:08:17.039><c> we</c><00:08:17.220><c> can</c><00:08:17.280><c> type</c>

00:08:17.510 --> 00:08:17.520 align:start position:0%
to do wirem two and three so we can type
 

00:08:17.520 --> 00:08:18.350 align:start position:0%
to do wirem two and three so we can type
in

00:08:18.350 --> 00:08:18.360 align:start position:0%
in
 

00:08:18.360 --> 00:08:21.110 align:start position:0%
in
we<00:08:18.780><c> can</c><00:08:18.900><c> get</c><00:08:19.020><c> the</c><00:08:19.199><c> list</c><00:08:19.440><c> and</c><00:08:20.400><c> we</c><00:08:20.639><c> can</c><00:08:20.759><c> also</c>

00:08:21.110 --> 00:08:21.120 align:start position:0%
we can get the list and we can also
 

00:08:21.120 --> 00:08:24.129 align:start position:0%
we can get the list and we can also
delete

00:08:24.129 --> 00:08:24.139 align:start position:0%
 
 

00:08:24.139 --> 00:08:26.570 align:start position:0%
 
now<00:08:25.139><c> the</c><00:08:25.379><c> interesting</c><00:08:25.740><c> part</c><00:08:25.979><c> that</c><00:08:26.280><c> we</c><00:08:26.460><c> don't</c>

00:08:26.570 --> 00:08:26.580 align:start position:0%
now the interesting part that we don't
 

00:08:26.580 --> 00:08:28.309 align:start position:0%
now the interesting part that we don't
have<00:08:26.759><c> much</c><00:08:27.000><c> time</c><00:08:27.300><c> to</c><00:08:27.539><c> explain</c><00:08:27.660><c> in</c><00:08:28.020><c> the</c><00:08:28.199><c> video</c>

00:08:28.309 --> 00:08:28.319 align:start position:0%
have much time to explain in the video
 

00:08:28.319 --> 00:08:30.469 align:start position:0%
have much time to explain in the video
is<00:08:28.680><c> how</c><00:08:28.979><c> we</c><00:08:29.220><c> actually</c><00:08:29.400><c> communicate</c><00:08:30.120><c> with</c><00:08:30.360><c> the</c>

00:08:30.469 --> 00:08:30.479 align:start position:0%
is how we actually communicate with the
 

00:08:30.479 --> 00:08:32.269 align:start position:0%
is how we actually communicate with the
server<00:08:30.780><c> read</c><00:08:31.379><c> this</c><00:08:31.560><c> section</c><00:08:31.800><c> for</c><00:08:32.099><c> more</c>

00:08:32.269 --> 00:08:32.279 align:start position:0%
server read this section for more
 

00:08:32.279 --> 00:08:33.969 align:start position:0%
server read this section for more
information

00:08:33.969 --> 00:08:33.979 align:start position:0%
information
 

00:08:33.979 --> 00:08:36.769 align:start position:0%
information
and<00:08:34.979><c> that's</c><00:08:35.159><c> how</c><00:08:35.399><c> to</c><00:08:35.580><c> create</c><00:08:35.820><c> a</c><00:08:36.360><c> minimalist</c>

00:08:36.769 --> 00:08:36.779 align:start position:0%
and that's how to create a minimalist
 

00:08:36.779 --> 00:08:38.990 align:start position:0%
and that's how to create a minimalist
single<00:08:37.260><c> layer</c><00:08:37.560><c> to-do</c><00:08:37.860><c> list</c><00:08:38.039><c> web</c><00:08:38.459><c> application</c>

00:08:38.990 --> 00:08:39.000 align:start position:0%
single layer to-do list web application
 

00:08:39.000 --> 00:08:41.990 align:start position:0%
single layer to-do list web application
with<00:08:39.300><c> the</c><00:08:39.419><c> ABP</c><00:08:39.839><c> framework</c><00:08:40.260><c> using</c><00:08:40.979><c> MVC</c><00:08:41.580><c> and</c>

00:08:41.990 --> 00:08:42.000 align:start position:0%
with the ABP framework using MVC and
 

00:08:42.000 --> 00:08:44.029 align:start position:0%
with the ABP framework using MVC and
mongodb

00:08:44.029 --> 00:08:44.039 align:start position:0%
mongodb
 

00:08:44.039 --> 00:08:46.880 align:start position:0%
mongodb
see<00:08:44.399><c> you</c><00:08:44.580><c> next</c><00:08:44.700><c> time</c>

"""
import re 
def clean_subtitles(subtitle_text):
    """
    This function takes subtitle text as input, removes the timestamp numbers,
    the header line, and returns a continuous text.

    Parameters:
    subtitle_text (str): The raw subtitle text.

    Returns:
    str: The cleaned continuous text.
    """
    # Split the text into lines
    lines = subtitle_text.splitlines()
    
    # Remove the first line if it contains the header information
    if lines and 'WEBVTT' in lines[0]:
        lines.pop(0)  # Remove the header line
    if 'Kind: captions' in lines[0]: 
        lines.pop(0)
    if 'Language:' in lines[0]:
        lines.pop(0)

    # Join the remaining lines into a single string
    cleaned_text = ' '.join(lines)

    # Regular expression to remove timestamps
    cleaned_text = re.sub(r'\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}', '', cleaned_text)
    
    # Remove HTML entities like &nbsp;
    cleaned_text = re.sub(r'&nbsp;', ' ', cleaned_text)
    
    # Replace multiple spaces with a single space and strip leading/trailing spaces
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

    return cleaned_text

def clean_again(text): 
    # Remove "align:start position:0%" and other align-related text
    cleaned_text = re.sub(r'align:start position:\d+% ', '', text)

    # Remove time codes and HTML tags
    cleaned_text = re.sub(r'<.*?>', '', cleaned_text)

    # Remove "[Music]" or similar annotations
    cleaned_text = re.sub(r'\[.*?\]', '', cleaned_text)

    # Strip extra whitespace and empty lines
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

        # Split the text into sentences
    sentences = cleaned_text.split(' ')
    
    # Remove duplicates while maintaining order
    seen = set()
    unique_sentences = []
    for sentence in sentences:
        if sentence not in seen:
            seen.add(sentence)
            unique_sentences.append(sentence)

    # Join the unique sentences back into a single string
    final_output = ' '.join(unique_sentences)

    return cleaned_text


cleaned_text = clean_subtitles(text2)
cleaned_text = clean_again(cleaned_text)
print(cleaned_text)
