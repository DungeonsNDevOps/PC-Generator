import .classes
import .races


class CharacterSheet:
    def __init__( self,
                  characterName:  None,
                  characterRace:  None,
                  characterClass: None ):


        self.Name  = characterName
        self.Race  = characterRace
        self.Class = CharacterClass


        ''' Class Traits '''
        try: 
            self.HitDice                     = self.Class\
                                                   .HitDie

            self.ArmorAndWeaponProficiencies = self.Class\
                                                   .ArmorAndWeaponProficiencies

            self.PrimaryAbility              = self.Class\
                                                   .PrimaryAbility

            self.SavingThrowProficiencies    = self.Class\
                                                   .SavingThrowProficiencies
        except Exception: return Exception


        ''' Racial Traits '''
        try:
            self.AbilityScore = self.Race\
                                    .traits\
                                    .AbilityScore

            self.Age          = self.Race\
                                    .traits\
                                    .Age

            self.Languages    = self.Race\
                                    .traits\
                                    .Languages

            self.Size         = self.Race\
                                   .traits\
                                   .Size

        except Exception: return Exception

