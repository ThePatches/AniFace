===================
 AniFace Readme
===================

What is AniFace
================

Aniface is an interface for keeping track of and watching downloaded
over a home network. It's called 'AniFace' because I'd orginally built it
to organize anime.

Installation
==============

Currently, the app is pluggable, but you need to change the directory
name to "``aniface``" for the links to work right. I am working on fixing
that change, but since this is my first attempt at Django, I'm having
more fun working on the whistles and bells.

Workflow
============
I am currently using a version of the workflow described `here
<http://nvie.com/git-model>`_. which eventually became *Git
Flow*, so I'll only list the workflows that will show up
frequently.

Master
-----------
This workflow represents the stable and final changes for the application
(going foward).

Clean-Up
-----------
This workflow is for cleaning up HTML issues. Anything that will affect the interface should be branched from here.

Quick-Fix
----------
If this branch shows up, it's because I've changed something quickly on *italics*Master*italics*
