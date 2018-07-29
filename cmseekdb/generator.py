#!/usr/bin/python3
# -*- coding: utf-8 -*-
# This is a part of CMSeeK, check the LICENSE file for more information
# Copyright (c) 2018 Tuhinshubhra

# Precise and Hawt

from html.parser import HTMLParser

ga = '0'
ga_content = ''

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if 'meta' in tag.lower():
            for nm,vl in attrs:
                if nm == "name" and vl.lower() == 'generator':
                    for a,b in attrs:
                        if a == 'content':
                            global ga, ga_content
                            ga = '1'
                            ga_content += ' ' + b

def parse(source):
    # clean up ga, ga_content (fix some weird multiple sites scan issue)
    global ga, ga_content
    ga = '0'
    ga_content = ''
    parser = MyHTMLParser()
    parser.feed(source)
    return [ga, ga_content]

def scan(content):
    content = content.lower()
    if content == '':
        return ['0', '']

    if 'wordpress' in content:
        # WordPress
        r = ['1','wp']
        return r

    if 'blogger' in content:
        # Blogger by google
        r = ['1','blg']
        return r

    if 'ghost' in content:
        # Ghost CMS
        r = ['1','ghost']
        return r

    if 'asciidoc' in content:
        # ASCiiDOC
        r = ['1','asciid']
        return r

    if 'drupal' in content:
        # Drupal
        r = ['1','dru']
        return r

    if 'bolt' in content:
        # Bolt CMS
        r = ['1','bolt']
        return r

    if 'browsercms' in content:
        # Browser CMS
        r = ['1','brcms']
        return r

    if 'ckan' in content:
        # CKAN
        r = ['1','ckan']
        return r

    if 'cms made simple' in content:
        # CMS Made Simple
        r = ['1','cmds']
        return r

    if 'cmsimple' in content:
        # CMSimple
        r = ['1','csim']
        return r

    if 'xpressengine' in content:
        # XpressEngine
        r = ['1','xe']
        return r

    if 'typo3 cms' in content:
        # TYPO3 CMS
        r = ['1','tp3']
        return r

    if 'textpattern cms' in content:
        # Textpattern CMS
        r = ['1','tpc']
        return r

    if 'ametys cms open source (http://www.ametys.org' in content:
        # Ametys CMS
        r = ['1','amcms']
        return r

    if 'joomla! - open source content management' in content or 'Joomla! - the dynamic portal engine and content management system' in content or 'joomla' in content:
        # Joomla
        r = ['1', 'joom']
        return r

    if 'xoops' in content:
        # XOOPS
        r = ['1', 'xoops']
        return r

    if 'wix.com' in content:
        # Wix Website Builder
        return ['1', 'wix']

    if 'cms: website baker' in content or 'www.websitebaker.org' in content:
        # Website Baker
        return ['1', 'wb']

    if 'webgui' in content:
        # WebGUI
        return ['1', 'wgui']

    if 'subrion cms' in content:
        # Subrion CMS
        return ['1', 'subcms']

    if 'tiki wiki cms groupware' in content or 'http://tiki.org' in content:
        # Tiki Wiki CMS Groupware
        return ['1', 'tiki']

    return ['0', '']
