basic_moves = {
    "kick_some_ass": {
        "miss_msg": """
        Well, fuck. At least I gain some experience.
        """,
        "hit_msg": """
            You and whatever you’re fighting inflict harm on each other. The amount of harm is based on the 
            established dangers in the game. That usually means you inflict the harm rating of your weapon and your 
            enemy inflicts their attack’s harm rating on you.
            """,
        "big_hit_msg": """
            You and whatever you’re fighting inflict harm on each other. The amount of harm is based on the 
            established dangers in the game. That usually means you inflict the harm rating of your weapon and your 
            enemy inflicts their attack’s harm rating on you.

            Choose one extra effect:
            • You gain the advantage: take +1 forward, or give +1 forward to another hunter.
            • You inflict terrible harm (+1 harm).
            • You suffer less harm (-1 harm).
            • You force them where you want them.
            """,
        "adv_hit_msg": """
            You and whatever you’re fighting inflict harm on each other. The amount of harm is based on the 
            established dangers in the game. That usually means you inflict the harm rating of your weapon and your 
            enemy inflicts their attack’s harm rating on you.

            Pick an enhanced effect:
            • You completely hold the advantage. All hunters involved in the fight get +1 forward.
            • You suffer no harm at all.
            • Your attack inflicts double the normal harm.
            • Your attack drives the enemy away in a rout.
            """,
    },
    "act_under_pressure": {
        "miss_msg": """
        Well, fuck. At least I gain some experience.
        """,
        "hit_msg": """
        The Keeper is going to give you a worse outcome, hard choice, or price to pay.
         """,
        "big_hit_msg": """
        You do what you set out to.
        """,
        "adv_hit_msg": """
        You may choose to either do what you wanted and something extra, or to do what you wanted to 
        absolute perfection.
        """,
    },
    "help_out": {
        "miss_msg": """
        Well, fuck. At least I gain some experience.
        """,
        "hit_msg": """
        Your help grants them +1 to their roll, but you also expose yourself to trouble or danger.
        """,
        "big_hit_msg": """
        Your help grants them +1 to their roll.
        """,
        "adv_hit_msg": """
        Your help lets them act as if they just rolled a 12, regardless of what they actually got.
        """,
    },
    "investigate": {
        "miss_msg": """
        Well, fuck. At least I gain some experience.
        """,
        "hit_msg": """
        Hold 1. 
        One hold can be spent to ask the Keeper one of the following questions:
        • What happened here?
        • What sort of creature is it?
        • What can it do?
        • What can hurt it?
        • Where did it go?
        • What was it going to do?
        • What is being concealed here?
        """,
        "big_hit_msg": """
        Hold 2. 
        One hold can be spent to ask the Keeper one of the following questions:
        • What happened here?
        • What sort of creature is it?
        • What can it do?
        • What can hurt it?
        • Where did it go?
        • What was it going to do?
        • What is being concealed here?
        """,
        "adv_hit_msg": """
         You may ask the Keeper any question you want about the mystery
        """,
    },
    "manipulate": {
        "miss_msg": """
        (Normal Person)
        Well, fuck. At least I gain some experience.
        
        (Another Hunter)
        It’s up to that hunter to decide how badly you offend or annoy them. 
        They mark experience if they decide not to do what you asked. Monsters and minions cannot normally 
        be manipulated.
        """,
        "hit_msg": """
        (Normal Person)
        They’ll do it, but only if you do something for them right now to show that you mean it. 
        If you asked too much, they’ll tell you what, if anything, it would take for them to do it.
        
        (Another Hunter)
        They mark experience if they do what you ask.
        """,
        "big_hit_msg": """
        (Normal Person)
        They’ll do it for the reason you gave them. If you asked too much, they’ll tell you the 
        minimum it would take for them to do it (or if there’s no way they’d do it).
        
        (Another Hunter)
        If they do what you ask they mark experience and get +1 forward.
        """,
        "adv_hit_msg": """
        (Normal Person)
        Not only do they do what you want right now, they also become your ally 
        for the rest of the mystery (or, if you do enough for them, permanently). 
        
        (Another Hunter)
        They must act under pressure to resist your request. If they do what you ask, 
        they mark one experience and take +1 ongoing while doing what you asked. 
        """,
    },
    "protect": {
        "miss_msg": """
        Well, fuck. At least I gain some experience.
        """,
        "hit_msg": """
        You protect them okay, but
        you’ll suffer some or all of the harm they
        were going to get. 
        """,
        "big_hit_msg": """
        Choose an extra:
        • You suffer little harm (-1 harm).
        • All impending danger is now focused on you.
        • You inflict harm on the enemy.
        • You hold the enemy back.
        """,
        "adv_hit_msg": """
        Both you and the character you are protecting are unharmed and out of danger. 
        If you were protecting a bystander, they also become your ally.
        """,
    },
    "read_a_situation": {
        "miss_msg": """
        Well, fuck. At least I gain some experience.
        """,
        "hit_msg": """
        Hold 1.
        One hold can be spent to ask the Keeper one of the following questions:
        • What’s my best way in?
        • What’s my best way out?
        • Are there any dangers we haven’t noticed?
        • What’s the biggest threat?
        • What’s most vulnerable to me?
        • What’s the best way to protect the victims?
        
        If you act on the answers, you get +1 ongoing while the information is relevant.
        """,
        "big_hit_msg": """
        Hold 3.
        One hold can be spent to ask the Keeper one of the following questions:
        • What’s my best way in?
        • What’s my best way out?
        • Are there any dangers we haven’t noticed?
        • What’s the biggest threat?
        • What’s most vulnerable to me?
        • What’s the best way to protect the victims?
        
        If you act on the answers, you get +1 ongoing while the information is relevant.
        """,
        "adv_hit_msg": """
        You may ask the Keeper any question you want about the situation, not just the listed ones.
        
        • What’s my best way in?
        • What’s my best way out?
        • Are there any dangers we haven’t noticed?
        • What’s the biggest threat?
        • What’s most vulnerable to me?
        • What’s the best way to protect the victims?
        """,
    },
    "magic": {
        "miss_msg": """
        Well, fuck. At least I gain some experience.
        """,
        "hit_msg": """
        It works imperfectly: 
        Choose your effect and a glitch. 
        The Keeper will decide what effect the glitch has.
        
        Effects:
        • Inflict harm (1-harm ignore-armour magic obvious).
        • Enchant a weapon. It gets +1 harm and +magic.
        • Do one thing that is beyond human limitations.
        • Bar a place or portal to a specific person or a type of creature.
        • Trap a specific person, minion, or monster.
        • Banish a spirit or curse from the person, object, or place it inhabits.
        • Summon a monster into the world.
        • Communicate with something that you  do not share a language with.
        • Observe another place or time.
        • Heal 1-harm from an injury, or cure a disease, or neutralize a poison.
        
        Glitches:
        • The effect is weakened.
        • The effect is of short duration.
        • You take 1-harm ignore-armour.
        • The magic draws immediate, unwelcome attention.
        • It has a problematic side effect.
        
        The Keeper may say that...
        • The spell requires weird materials.
        • The spell will take 10 seconds, 30 seconds, or 1 minute to cast.
        • The spell requires ritual chanting and gestures.
        • The spell requires you to draw arcane symbols.
        • You need one or two people to help cast the spell.
        • You need to refer to a tome of magic for the details.
        """,
        "big_hit_msg": """
        The magic works without issues: choose your effect.
                
        Effects:
        • Inflict harm (1-harm ignore-armour magic obvious).
        • Enchant a weapon. It gets +1 harm and +magic.
        • Do one thing that is beyond human limitations.
        • Bar a place or portal to a specific person or a type of creature.
        • Trap a specific person, minion, or monster.
        • Banish a spirit or curse from the person, object, or place it inhabits.
        • Summon a monster into the world.
        • Communicate with something that you do not share a language with.
        • Observe another place or time.
        • Heal 1-harm from an injury, or cure a disease, or neutralize a poison.
        """,
        "adv_hit_msg": """
        The Keeper will offer you some added benefit in addition to:
                
        Effects:
        • Inflict harm (1-harm ignore-armour magic obvious).
        • Enchant a weapon. It gets +1 harm and +magic.
        • Do one thing that is beyond human limitations.
        • Bar a place or portal to a specific  person or a type of creature.
        • Trap a specific person, minion, or monster.
        • Banish a spirit or curse from the person, object, or place it inhabits.
        • Summon a monster into the world.
        • Communicate with something that you do not share a language with.
        • Observe another place or time.
        • Heal 1-harm from an injury, or cure a disease, or neutralize a poison.
        """,
    },
    "big_magic": {
        "msg": """
        Use this when you want more than the Use Magic effects. 
        Tell the Keeper what you want to do.
        
        The Keeper may require:
        • You need to spend a lot of time (days or weeks) researching the magic ritual.
        • You need to experiment with the spell – there will be lots of failures before you get it right.
        • You need some rare and weird ingredients and supplies.
        • The spell will take a long time (hours or days) to cast.
        • You need a lot of people (2, 3, 7, 13, or more) to help.
        • The spell needs to be cast at a particular place and/or time.
        • You need to use magic as part of the ritual, perhaps to summon a monster, communicate with something, 
        or bar the portal you opened.
        • It will have a specific side-effect or danger.
        
        If you meet the requirements, then the magic takes effect.
        """
    },
    "harm": {
        "msg": """
        Whenever you suffer harm, the Keeper
        will tell you what effect it has.
        Injury severity depends on how much
        harm you have suffered:
        • 0-harm wounds have only minor,
        short term effects.
        • 4-7 harm wounds are serious
        and unstable. They will get
        worse unless treated. Mark the
        “Unstable” box.
        • 8-harm or more will kill a normal
        human, including a hunter.
        Armour reduces the harm suffered by
        the number of points it is rated for.
        Monsters may not be defeated until
        you use their weakness against them,
        and this applies to some minions as well.
        """
    },
    "recovery": {
        "msg": """
        • 0 harm wounds are considered healed right away.
        • 1-3 harm wounds improve when you receive first aid, 
        and later when you rest. Heal 1 when you do.
        • Unstable wounds require first aid to become stable. 
        While unstable, they may get worse.
        • 4+ harm wounds require a healing move, time in an 
        infirmary or hospital, or magical healing.
        
        At the end of the mystery, you also have a chance to heal.
        • If there is no chance to rest, heal 1 harm.
        • If there is plenty of time, heal all harm.
        """
    },
    "luck": {
        "msg": """
        You may:
        Decrease a wound you have suffered to 0 harm.
        After you roll, retroactively change the result to a 12.
        """,
        "out_of_luck_msg": """
        You are out of luck.
        Bad things will happen to you.
        """,
    },
}
