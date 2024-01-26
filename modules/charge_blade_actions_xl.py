def get_charge_blade_actions_xl(charge_blade):
    return [
        # Row 1
        {
            "index": 0,
            "icon": "charge_sword.png",
            "label": "Charge Sword",
            "action": charge_blade.charge_sword,
        },
        {
            "index": 2,
            "icon": "charge_phials.png",
            "label": "Bank It",
            "action": charge_blade.bank_it,
        },

        # Row 2
        {
            "index": 8,
            "icon": "charge_shield.png",
            "label": "Charge Shield",
            "action": charge_blade.charge_shield,
        },
        {
            "index": 11,
            "icon": "charge_shield_sword.png",
            "label": "Charge Shield & Sword",
            "action": charge_blade.charge_shield_sword,
        },

        # Row 3
        {
            "index": 16,
            "icon": "Fill_Phials_1.png",
            "label": "Fill Phials Far",
            "action": charge_blade.fill_phials,
        },
        {
            "index": 17,
            "icon": "Fill_Phials_2.png",
            "label": "Fill Phials Near",
            "action": charge_blade.fill_phials_2,
        },
        {
            "index": 18,
            "icon": "SAED_2.png",
            "label": "SAED 2",
            "action": charge_blade.saed_combo_2,
        },
        {
            "index": 19,
            "icon": "Savage_Axe_Finisher_2.png",
            "label": "S. Axe Combo",
            "action": charge_blade.savage_axe_combo,
        },

        # Row 4
        {
            "index": 24,
            "icon": "Combo_1.png",
            "label": "Full Combo Far",
            "action": charge_blade.charge_blade_sword_combo,
        },
        {
            "index": 25,
            "icon": "Combo_2.png",
            "label": "Full Combo Near",
            "action": charge_blade.charge_blade_sword_combo_2,
        },
        {
            "index": 26,
            "icon": "SAED_1.png",
            "label": "SAED",
            "action": charge_blade.saed_combo,
        },
        {
            "index": 27,
            "icon": "Savage_Axe_Finisher_1.png",
            "label": "S. Axe Finisher",
            "action": charge_blade.savage_axe_finisher,
        },
    ]
