#
# Copyright 2016 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Generates a list of historical event dates that may have had
significant impact on markets.  See extract_interesting_date_ranges."""

import pandas as pd

from collections import OrderedDict

PERIODS = OrderedDict()
# Dotcom bubble
PERIODS['Dotcom'] = (pd.Timestamp('20000310').tz_localize('UTC'),
                     pd.Timestamp('20000910').tz_localize('UTC'))

# Lehmann Brothers
PERIODS['Lehman'] = (pd.Timestamp('20080801').tz_localize('UTC'),
                     pd.Timestamp('20081001').tz_localize('UTC'))

# 9/11
PERIODS['9/11'] = (pd.Timestamp('20010911').tz_localize('UTC'),
                   pd.Timestamp('20011011').tz_localize('UTC'))

# 05/08/11  US down grade and European Debt Crisis 2011
PERIODS[
    'US downgrade/European Debt Crisis'] = (
    pd.Timestamp('20110805').tz_localize('UTC'),
    pd.Timestamp('20110905').tz_localize('UTC'))

# 16/03/11  Fukushima melt down 2011
PERIODS['Fukushima'] = (pd.Timestamp('20110316').tz_localize('UTC'),
                        pd.Timestamp('20110416').tz_localize('UTC'))

# 01/08/03  US Housing Bubble 2003
PERIODS['US Housing'] = (
    pd.Timestamp('20030108').tz_localize('UTC'),
    pd.Timestamp('20030208').tz_localize('UTC'))

# 06/09/12  EZB IR Event 2012
PERIODS['EZB IR Event'] = (
    pd.Timestamp('20120910').tz_localize('UTC'), pd.Timestamp('20121010').tz_localize('UTC')
)

# August 2007, March and September of 2008, Q1 & Q2 2009,
PERIODS['Aug07'] = (pd.Timestamp('20070801').tz_localize('UTC'),
                    pd.Timestamp('20070901').tz_localize('UTC'))
PERIODS['Mar08'] = (pd.Timestamp('20080301').tz_localize('UTC'),
                    pd.Timestamp('20080401').tz_localize('UTC'))
PERIODS['Sept08'] = (pd.Timestamp('20080901').tz_localize('UTC'),
                     pd.Timestamp('20081001').tz_localize('UTC'))
PERIODS['2009Q1'] = (pd.Timestamp('20090101').tz_localize('UTC'),
                     pd.Timestamp('20090301').tz_localize('UTC'))
PERIODS['2009Q2'] = (pd.Timestamp('20090301').tz_localize('UTC'),
                     pd.Timestamp('20090601').tz_localize('UTC'))

# Flash Crash (May 6, 2010 + 1 week post),
PERIODS['Flash Crash'] = (
    pd.Timestamp('20100505').tz_localize('UTC'),
    pd.Timestamp('20100510').tz_localize('UTC'))

# April and October 2014).
PERIODS['Apr14'] = (pd.Timestamp('20140401').tz_localize('UTC'),
                    pd.Timestamp('20140501').tz_localize('UTC'))
PERIODS['Oct14'] = (pd.Timestamp('20141001').tz_localize('UTC'),
                    pd.Timestamp('20141101').tz_localize('UTC'))

# Market down-turn in August/Sept 2015
PERIODS['Fall2015'] = (pd.Timestamp('20150815').tz_localize('UTC'),
                       pd.Timestamp('20150930').tz_localize('UTC'))

# Market regimes
PERIODS['Low Volatility Bull Market'] = (
    pd.Timestamp('20050101').tz_localize('UTC'),
    pd.Timestamp('20070801').tz_localize('UTC'))

PERIODS['GFC Crash'] = (pd.Timestamp('20070801').tz_localize('UTC'),
                        pd.Timestamp('20090401').tz_localize('UTC'))

PERIODS['Recovery'] = (pd.Timestamp('20090401').tz_localize('UTC'),
                       pd.Timestamp('20130101').tz_localize('UTC'))

PERIODS['New Normal'] = (pd.Timestamp('20130101').tz_localize('UTC'),
                         pd.Timestamp('today').tz_localize('UTC'))
