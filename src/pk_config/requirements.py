# -*- coding: utf-8 -*-

__all__ = [ 'Requirements' ]

import sys
import os
import inspect

from pkg_resources import (
    DistributionNotFound,
    Requirement, Environment,
    require, get_distribution,
    working_set
)

class Requirements(object) :

    def __init__(self) :
        self._caller = ''
        self._requirements = []
        self._locations = []
        self._environment = Environment()
        self._missing_distribs = []
        
        stack = list(
            filter(
                lambda s :
                    inspect.getframeinfo(s[0]).code_context is not None
                    and inspect.getframeinfo(s[0]).function == '<module>', 
                inspect.stack()
            )
        )

        try :
            self._caller = os.path.realpath(
                inspect.getfile(stack[-1][0])
            )
        except IndexError as e :
            pass

        self._req_file = self.caller.replace('.py', '.req')

        try :
            with open(self.req_file) as fp :
                self._requirements = [ Requirement.parse(req) for req in fp.readlines() ]  
        except FileNotFoundError as e :
            pass

        self.search()

    def __getitem__(self, name) :
        return self.environment[name]

    @property
    def environment(self) :
        return self._environment

    @property
    def locations(self) :
        return self._locations

    @property
    def requirements(self) :
        return self._requirements

    @property
    def missing_distribs(self) :
        return self._missing_distribs
            
    @property
    def caller(self) :
        return self._caller

    @property
    def req_file(self) :
        return self._req_file

    def add(self, requirement) :
        self._requirements.append(Requirement.parse(requirement))
        self.search()

    def add_location(self, location) :
        self._locations.append(location)
        self.search()

    def search(self) :
        places = []
        for r in self.requirements :
            for l in self.locations :
                places.append(l)
                places.append(l + '/' + r.name)
                
        return self.environment.scan(places)

    def satisfy(self) :
        self._missing_distribs = []
        self.search()

        for requirement in self.requirements :
            try :
                # distrib disponible directement ?
                distrib = get_distribution(requirement)
                self.environment.add(distrib)

            except DistributionNotFound as e :
                # meilleur candidat pour cette distrib aux emplacements désignés
                distrib = self.environment.best_match(
                    requirement,
                    working_set
                )
                if distrib is not None :
                    working_set.add(distrib)
                else :
                    self._missing_distribs.append(requirement)

        if len(self.missing_distribs) > 0 :
            print(
                'Missing distributions : ', list(map(str, self.missing_distribs)),
                file=sys.stderr
            )
            return False

        return True

        
