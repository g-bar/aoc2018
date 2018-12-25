from dataclasses import dataclass, field
from collections import defaultdict
from typing import Any
import re

@dataclass(eq=False)
class Group:    
    units: int
    hp: int    
    attack: int
    damage_type: str
    initiative: int
    weak_to: list = field(default_factory=list)
    immune_to: list = field(default_factory=list)
    targets: list = field(default_factory=list, repr=False)
    target: Any = field(default = None, repr = False)

    @property
    def effective_power(self):
        return self.units * self.attack

    def damage(self, other):
        if other.damage_type in self.immune_to:
            return 0
        elif other.damage_type in self.weak_to:
            return other.effective_power * 2
        else:
            return other.effective_power
    
    def iter_targets(self):
        yield from sorted(self.targets, key= lambda t: (t.damage(self), t.effective_power, t.initiative), reverse=True)

if __name__ == "__main__":
    use_example = False
    fname = 'day24_input.txt' if not use_example else 'day24_example.txt'
    
    pattern = re.compile(r'(?P<units>\d+) units each with (?P<hp>\d+) hit points(?: \((?P<features>.+)\))? with an attack that does (?P<attack>\d+) (?P<damage_type>\w+) damage at initiative (?P<initiative>\d+)')
    
    words = re.compile(r'\w+')
    
    def _units(groups):
        return [sum(g.units for g in s) for s in groups.values()]

    def battle(boost=0):
        groups = {'Immune':set(), 'Infection': set()}
        for line in open(fname):
            if 'Immune' in line:
                band = "Immune"
                target = 'Infection'
                continue
            elif 'Infection' in line:
                band = "Infection"
                target = 'Immune'
                continue
            
            match = pattern.match(line)
            if match is None:
                continue
            
            d = {k:int(v) if v and v.isdigit() else v for k,v in match.groupdict().items()} 
            if band == 'Immune':
                d['attack'] += boost

            f = d.pop('features')
            if f:
                
                for el in f.split(';'):                
                    if 'weak to' in el:
                        d['weak_to'] = words.findall(el)[2:]
                    elif 'immune to' in el:
                        d['immune_to'] = words.findall(el)[2:]
            
            g = Group(**d, targets = groups[target])
            groups[band].add(g)

        while all(groups.values()):
            
            #Target selection
            under_attack = set()
            for g in sorted(groups['Immune'] | groups['Infection'], key=lambda i: (i.effective_power, i.initiative), reverse=True):
                g.target = None
                for t in g.iter_targets():
                    
                    if t.damage(g) == 0:
                        break
                    if t not in under_attack:
                        g.target = t
                        under_attack.add(t)
                        break
            
            units = _units(groups)
            

            for g in sorted(groups['Immune'] | groups['Infection'], key=lambda i: i.initiative, reverse = True):
                
                if g.target and g.target.units > 0 and g.units>0:
                    damage = g.target.damage(g)
                    g.target.units -= damage // g.target.hp
                    
                    if g.target.units <= 0:
                        for s in groups.values():
                            s.discard(g.target)
            
            if _units(groups) == units:
                return None, None
                        
        return sum(g.units for s in groups.values() for g in s), 'Immune' if groups['Immune'] else 'Infection'

# Part 1
print(battle())

# Part 2

winner = None
boost = 1
while winner != 'Immune':    
    nunits, winner = battle(boost)
    print(f'Boost: {boost}, units: {nunits}, winner: {winner}')
    boost+=1

print(nunits)
