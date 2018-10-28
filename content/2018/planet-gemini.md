Title: Review of the Gemini PDA
Authors: dtsomp
Date: 2018-10-28
Summary: It's huge, it's weird, it has a physical keyboard, it runs Linux. Of course I got one.

I have recently received help to my eternal effort of collecting weird gadgets.
The Planet Gemini's [Indiegogo campaign](https://www.indiegogo.com/projects/gemini-pda-android-linux-keyboard-mobile-device--2#/) went brilliantly, they entered production and I received my device a few months ago. 

![gemini_open](/images/2018/gemini/open.jpg)

Initially, the Gemini PDA sat on my desk for weeks, unused - hard to focus on gadgets with a newborn in your lap.
But the last two-three weeks I've been using it more and more, from day-to-day commuting to travelling abroad.
Here's my opinion on it.

## What is it?

[Planet Computers](https://www.planetcom.co.uk/) is a company founded by the people that built the [Psion PDAs](https://en.wikipedia.org/wiki/Psion_Series_5) in the 90s.
Apparently, they thought the market needed more physical keyboards on mobile devices, so they lauched an Indiegogo campaign to fund their new device - the Gemini PDA.

The Gemini is a PDA, as in "not a tablet, but not a smartphone either".
It's very smartphone-ish, but cellular connectivity is actually optional.
If it helps, think of it as an iPod Touch with a keyboard.

It runs Android on a 10-core Cortex CPU and it runs all of your favorite Android apps.
To support the PDA moniker, there are built-in apps for tasks, calendars and notes.
For the tinkerers out there, the Gemini can be modified to boot into Debian or Sailfish OS.

## Getting physical

The first thing you notice about the device is its size and weight.
At 320gr, it's easily more than 2x the weight of my daily driver, a Google Pixel.
It's also double the Pixel's thickness and over 3cm longer.
The word "brick" tends to come up often.

Here's what it looks like side by side to a Google Pixel and an iPad Mini.

![gemini_front](/images/2018/gemini/size-compare-front.jpg)
![gemini_side](/images/2018/gemini/size-compare-side.jpg)

Open up the lid of the device and there's a 6-inch screen, which would be impressive on its own,
but the keyboard below it grabs any and all attention.

It's a big, physical, clicky QWERTY keyboard. 

![keyboard](/images/2018/gemini/keyboard.jpg)

Physical, with tactile feedback, key travel and everything.
It's a tiny version of a normal laptop keyboard, 
but using multiple fingers on the keyboard is definitely possible.

Almost all symbol keys have been rearranged and a lot of them require the Fn key,
which is understandable - the real-estate on the device is little and precious and some compromises had to be made.
On the positive side, the keyboard is actually... good!
The key travel is arguably a bit too much (you've never read this about a phone before, did you?) and it slows down typing a bit, but maybe that's on purpose - I guess it'd be weird to have people hammer the tiny (but not too tiny) keys.
The sound of clicky-clicky-click on a phone is an ultra-rare experience and I actually like it,
but you should forget about using the keyboard during the night next to a sleeping spouse or baby.
It's not loud by any measure, but it's there, and that's probably enough.

Typing long-winded texts (like blog posts) is probably pushing the limits of the device.
It's not that it can not handle it, but the keyboard is not comfortable enough for long typing sesions and your hands will get tired.
Practice makes perfect, but still, it's not your full-size laptop.

On the other hand, occasional sysadmin work on it is wonderful.
SSHing to a server and troubleshooting issues is perfectly doable,
so much better than any phone with an on-screen virtual keyboard or a thumb keyboard.

Physically extending the device is perfectly possible.
There is a micro-SD slot, so plenty of options on expanding the 64GB of storage that is on-board.
There are two (TWO!) USB-C ports, for charging and extending your tiny laptop.
My USB-C-to-USB-A converter works perfectly and devices like mice, keyboards, Ethernet adapters and SD card readers worked out of the box.

Everybody should get one of these:
![adapter](/images/2018/gemini/adapter.jpg)

HDMI out is a different issue - read below, under "[Screen time](#screentime)"

## Getting connected

There are two versions of the device: the plain non-cellular one and the 4G-enabled one.
I opted to get the 4G-enabled device, which comes with a micro-SIM slot plus eSIM.

I don't have any eSIM subscriptions, but I've tested with 3 SIM cards.
4G worked out of the box with all of them.
On every SIM change, a popup will let you know that you need to configure which SIM (the microSIM or the eSIM) will take care of outgoing calls and messages.
Usually, it already knows what it needs to do, so you just end up confirming that it did well.
I like it.

Note: the tool for popping up the lid that covers the SIM and microSD slots is a HUGE METAL SLAB.

I mean it.

![sim_tool](/images/2018/gemini/sim_tool.jpg)

Taking the lid off and putting it on again is in no way an experience that makes you feel comfortable.
It's easy enough, but it's quite scary to hear the sound of multiple metal hinges releasing all at the same time.

More on networking:
There's wifi with 802.11 a/b/g/n/ac support, Bluetooth 4.1, Assisted GPS.
They work as intended, nothing more to add.

Sadly, there's no NFC.

##<a name="screentime"></a> Screen time

It's ok.

The screen is a fairly imposing 6 inches of diagonal length, so there's plenty of area on this baby.
The resolution is not bad - 2160x1080, translating to 403ppi. 
You can definitely tell that there are plenty pixels to go around when you boot into Debian - everything is super tiny.
It's just that Android seems to waste the high resolution and everything is a bit on the large side.
The problem becomes a bit more apparent when you rotate the screen to portrait mode. 
Icons look a bit too large and out of place and there's something just a bit wrong about how scaling works in Android.
Or... it's just me and my eyes, both accustomed to using the Google Pixel all day long.

I should be seeing more information, right?

![portrait.png](/images/2018/gemini/portrait.png)

The issue of rotation is something that keeps on giving a weird vibe.
On the Gemini, the Android desktop is pinned to landscape-mode because... reasons?

Switching to portrait requires the following steps: 

- bring up the Gemini taskbar (Alt key)
- tap the Planet menu icon
- tap Force Rotate

![force_rotate.png](/images/2018/gemini/force_rotate.png)

There's no way to lock that down, so closing the lid and re-opening will go back to landscape mode.
I guess we have to live with that.

The screen quality is not the greatest, it's definitely classes behind my Google Pixel.
But it's not bad either, it's just... ok.
To be honest, if you don't have a high-end device to compare it with, you'll probably never notice it.
Overall, it's good enough.

To fulfill the "tiny laptop" promise, one of the two USB-C ports (the right-hand one) has support for HDMI output.
I've tried with a few third-party adapters and none has worked so far.
On the contrary, some of them consistenly caused reboots of the device.
Eventually, I had to accept defeat and order the Planet-branded adapter, which works As Seen On TV.

Running Android on a 24-inch computer screen or a 40-inch TV is ridiculous and weird and fantastic, all at the same time.
Plugging a USB-C hub (better luck with 3rd party ones here) with a mouse and keyboard turns this into a full-fledged desktop,
and if your work is just SSH/Google Docs/email, I don't see how this would not work as a day-to-day machine.

## Photography

The camera module is optional.
I didn't go for it, so no camera for me.

There is a user-facing camera, next to the screen.
I'm not happy with it, but I can't say I care about it either.

Moving on.

## Actually using the device

Typing and working on the tiny laptop - ahem, PDA - is what it does best.
It's infintely easier to type on it when it rests on a flat surface, but thumb-typing also works fairly good, just not as fast.

Browsing is weird, mostly because the default orientation is landscape, so you only get to see a few lines of web page material. 
That means you should expect a lot of scrolling.

As already mentioned, switching to portrait kind of fixes this, but it's not straighforward or intuitive, and there's also the issue of how to actually hold a device with a keyboard on the side.
Interestingly, portrait is available one way only: the desktop rotates counter-clockwise 90 degrees, so that the keyboard ends up to the left of the screen.
Holding the device like this takes getting used to it, since the keyboard part is fairly heavy and throws the balance of your grip off.

Typing with a rotated keyboard on the left of the screen while in portrait is annoying, so portrait orientation should only be used for long scrolling sessions on the browser or games.

For the brave ones that plan to use the Gemini as a phone, be warned: there will be a lot of opening/closing the clamshell device.
There is no screen on the outside of the device, just the notification LEDs.
Caller ID and proper Android notifications all show up in the big 6" screen, on the inside of the device, which means you'll need to open the device to check every notification.
Planet ships a LED configurator app with the Gemini, so you can 

The only way to interact with the device without opening it first is to use the single external button that either activates Google Voice Assistant or answers a call.
Using a smartwatch as a notification terminal is probably the easiest way around all this fuss.

When you eventually answer or place a call on the device, you need to close down the lid and hold it as any other handset.
This is also a new experience, since there is no specific end to speak to.
Planet has placed a microphone and speaker on both ends of the device, so you can just use it any way you like.
The device will detect automatically which end you're talking to and configure things accordingly.
This works mostly ok, except when I am in a noisy environment or I speak too softly. 

Apart from that, the call quality was not very good and I am not particularly happy with it. 

The Gemini is not as courageous as an iPhone, so it still has a headphone jack.
Sadly, it's pretty bad and there's a lot of static and the sound quality is low.
I am 90% sure there is a problem with my device specifically and I do hope it's that - because messing up the headphone jack this bad is unheard of.

I don't own a pair of Bluetooth headphones to test, but BT has performed pretty well in other aspects, so I am going to go ahead and assume audio over BT is probably the best choice.

## OS galore

The Gemini comes pre-loaded with Android.
As expected from a small manufacturer with limited resources, it's not running the latest and greatest of Android.
My device is currently on Android 7.1.1 and while there is a minor version update available, I can not install this using the Firmware Update tool in Android,
because I have decided to make things hard for me and went ahead and made the device dual-boot to Android and Debian.
That requires resizing the partitions, which apparently the OTA updater does not particularly like.
Before doing the dual-boot tango, updating worked fine, so I am willing to accept a small percentage of blame here, although I would still very much like to have OTA updates regardless of number of boot options.

Speaking of dual-booting...

Planet has purposefully marketed the device as capable of running multiple OSes.
The list for the time being seems to be:

- Android
- rooted Android
- Debian
- Sailfish OS

They've even made a handy little [partition tool](http://support.planetcom.co.uk/partitionTool.html) to help out with flashing the device.
The process is not that easy, so make sure to follow the [official Linux flashing guide](http://support.planetcom.co.uk/index.php/Linux_Flashing_Guide).

Flashing the device will erase any previous data, but will get you a pretty little device running Debian, and that's something we all dream about :)

The full desktop Linux experience on a device of this size is awkward but SO FREAKING COOL.
Things are not snappy, performance reminded me of a Raspberry Pi 3, but it's still a full Linux desktop in the palm of your hands.

The Debian installation is a custom one, tailor-made by the Planet team, so everything hardware-wise works out of the box.
There's room for improvement - especially in the power management area, but overall things work smoothly, just a bit slow.
The Debian version is 9.5 and the default desktop environment is LXQt.
Some menus require that you drag your finger across menu popups instead of tapping the things you want, so I quickly thought this is a good opportunity to test out my el-cheapo Bluetooth mouse.
A bit of manual configuration later, it worked:

![linux.jpg](/images/2018/gemini/linux.jpg)

The Linux installation comes pre-loaded with LibreOffice and Chromium, so it's dead easy to start getting work done with it.
I got git and pelican running on it immediately, so part of this review is actually written on a Linux-running Gemini.

## Battery life

The built-in battery is 4000something mAh. That's a lot.

I have not used the device heavily, so I am not sure what a maniac would get ouf it, but light use wields 5+ days.
With cellular connectivity running but without me using the device, standby reaches double-digits.
I am just going to assume that a Gemini with all radios off can do standby for weeks.

I love sending this screenshot to friends that spend a good part of their life trying to make their smartphones reach 24 hours of battery.
![battery.png](/images/2018/gemini/battery.png)

Booting into Linux has a bigger impact on battery life and it's definitely not measured in days any more.
I'll be honest, I haven't had the patience to deplete the battery on Linux (life keeps getting in the way), but if I had to estimate, I'd say circa 8-10 hours, not unlike a decent laptop experience.

All in all, I am more than happy with the battery life.

## Conclusion

The Gemini is both great and useless. I love it :)

One of the best usage experiences I got from the Gemini was when I had to handle a production issue at **$Work** while at a cafe, on a Saturday.
Similarly to my previous mobile devices, I installed the VPN client and the SSH client and got down to business.
The difference here was that I didn't have a virtual keyboard to get in the way and I didn't have to balance my device and thumb-type towards system stability.
I set the Gemini on my coffee table and got to work.

It was so much easier than any other mobile device (smartphone or tablet) I've used for this purpose.

![ssh.png](/images/2018/gemini/ssh.png)

On the other hand, I don't see any realistic scenario where someone would use this as their primary phone. 
It's heavy, it doesn't fit in a lot of pockets and using the phone capabilities is a PITA.
As a second phone, it's OK, although carrying both the Gemini and another phone will still require large pockets or a man-purse.

I think that the Gemini sits in the tiny niche between smartphones and 8" tablets, especially the iPad Mini.
Whether that niche is called "PDA" or something else is debatable.

In the past I've tried using an Android tablet with a BT keyboard as a laptop substitute and it just didn't work for me.
There were too many cables and things to carry around and it just annoyed me that I still didn't get anything productive done because, among everything else, Android is fairly bad on tablets.
The iPad Mini runs a much better OS for tablet use, but the amount of accessories needed is still the same. 

The Gemini seems to be a better package, just because it brings its own keyboard with it and runs Android like a phone would.
The performance might not be top of the line, but it's good, good enough for light work, and it still fits in my jacket pocket.

The added value of sharing a USB-C charger with my primary phone means I only need to carry one charger. 
That makes the Gemini my current favorite travel laptop.

To be honest, this is a very *sysadmin* device.
It really is intended for people that could do with a netbook but find typing on a tablet's screen appalling.

