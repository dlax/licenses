class LicenseList(object):
    okd_compliant = [
        u'Open Data Commons Public Domain Dedication and License (PDDL)',
        u'Open Data Commons Open Database License (ODbL)',
        u'Creative Commons CCZero',
        u'Creative Commons Attribution',
        u'Creative Commons Attribution-ShareAlike',
        u'GNU Free Documentation License (GFDL)',
        u'UK Click Use PSI',
        u'Other',
        ]

    okf_compliant_formatted = [ u'OKD Compliant::' + x for x in okd_compliant ]

    non_okd_compliant = [
        u'Creative Commons Non-Commercial (Any)',
        u'Non-Commerical Other',
        u'Other',
        ]

    non_okd_compliant_formatted = [ u'Non-OKD Compliant::' + x for x in non_okd_compliant]
    
    other = [
        u'License Not Specified'
        ]

    other_formatted = [ u'Other::' + x for x in other ]

    osi_approved = [
        # main ones
        u'New BSD license',
        u'GNU General Public License (GPL)',
        u'GNU General Public License v3 (GPLv3)',
        u'GNU Library or "Lesser" General Public License (LGPL)',
        u'MIT license',
        # rest are alphabetical
        u'Academic Free License',
        u'Adaptive Public License',
        u'Apache Software License',
        u'Apache License, 2.0',
        u'Apple Public Source License',
        u'Artistic license',
        u'Attribution Assurance Licenses',
        u'Computer Associates Trusted Open Source License 1.1',
        u'Common Development and Distribution License',
        u'Common Public License 1.0',
        u'CUA Office Public License Version 1.0',
        u'EU DataGrid Software License',
        u'Eclipse Public License',
        u'Educational Community License',
        u'Eiffel Forum License',
        u'Eiffel Forum License V2.0',
        u'Entessa Public License',
        u'Fair License',
        u'Frameworx License',
        u'IBM Public License',
        u'Intel Open Source License',
        u'Jabber Open Source License',
        u'Lucent Public License (Plan9)',
        u'Lucent Public License Version 1.02',
        u'MITRE Collaborative Virtual Workspace License (CVW License)',
        u'Motosoto License',
        u'Mozilla Public License 1.0 (MPL)',
        u'Mozilla Public License 1.1 (MPL)',
        u'NASA Open Source Agreement 1.3',
        u'Naumen Public License',
        u'Nethack General Public License',
        u'Nokia Open Source License',
        u'OCLC Research Public License 2.0',
        u'Open Group Test Suite License',
        u'Open Software License',
        u'PHP License',
        u'Python license (CNRI Python License)',
        u'Python Software Foundation License',
        u'Qt Public License (QPL)',
        u'RealNetworks Public Source License V1.0',
        u'Reciprocal Public License',
        u'Ricoh Source Code Public License',
        u'Sleepycat License',
        u'Sun Industry Standards Source License (SISSL)',
        u'Sun Public License',
        u'Sybase Open Watcom Public License 1.0',
        u'University of Illinois/NCSA Open Source License',
        u'Vovida Software License v. 1.0',
        u'W3C License',
        u'wxWindows Library License',
        u'X.Net License',
        u'Zope Public License',
        u'zlib/libpng license',
        ]

    osi_approved_formatted = [ u'OSI Approved::' + x for x in osi_approved]

    all_formatted = other_formatted + okd_compliant_formatted + \
        non_okd_compliant_formatted + osi_approved_formatted
