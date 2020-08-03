#!/usr/bin/env python
#
# (C) Copyright 2012-2013 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0. 
# In applying this licence, ECMWF does not waive the privileges and immunities 
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.
#

from ecmwfapi import ECMWFDataServer
# To run this example, you need an API key
# available from https://api.ecmwf.int/v1/key/
 
server = ECMWFDataServer()
  
start_date=20180101
end_date=20180331
date=str(start_date) + '/to/' + str(end_date)
targetname=str(start_date) + '_to_' + str(end_date)

server.retrieve({
          'dataset' : "interim",
          'date'    : "%s"%(date),
          'time'     : "00/06/12/18",
          'step'     : "0",
          'stream'   : "oper",
          'levtype'  : "sfc",
          'levelist' : "all",
          'type'     : "an",
          'class'    : "ei",
          'grid'     : "128",
          'param'    : "134",
          'target'   : "surf_2018_jan_feb_mar.grb"		
          })
