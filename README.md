
Django Bootrap Base - HTML5 Boilerplate
================================

This provides a base template bootstrap-base/html5pb.html for your own base_site.html to extend.

It is based on http://initializr.com/

All js and css are included in static/bootstrap-base for use with collectstatic.

All blocks can be customized so you can swap different bootstraps in.

Uses the {% static .. %} tag so this is Django 1.4+

The goal is to be able to work on bootstrap sites with the minimum of fiddling to set up and yet not be constrained from customizing anything.  Any improvements or new-fangled things should be able to propagate to all sites.


Install
-------

Add it to your INSTALLED_APPS below your site's app.


Blocks
------

* title
* meta-tags
* style-libraries
	* 	defaults to: boostrap + responsive v2.1.1
* styles
* extrahead
*  modernizr
	* 	defaults to: modernizer.js

* navbar
	* 	navbar-inner
    	* 	defaults to: a generic menu

* container
	*  content
	*  footer

* script-libraries
	*	defaults to: jquery 1.8, boostrap.min.js
* scripts
* analytics
	* ua


