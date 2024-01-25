def get_charge_blade_actions_original(charge_blade):
    return [
        {
            "index": 0,
            "icon": "charge_sword.png",
            "label": "Charge Sword",
            "action": charge_blade.charge_sword,
        },
        {
            "index": 1,
            "icon": "charge_shield.png",
            "label": "Charge Shield",
            "action": charge_blade.charge_shield,
        },
        {
            "index": 4,
            "icon": "charge_phials.png",
            "label": "Bank It",
            "action": charge_blade.bank_it,
        },
        {
            "index": 5,
            "icon": "Fill_Phials_1.png",
            "label": "Fill Phials Far",
            "action": charge_blade.fill_phials,
        },
        {
            "index": 6,
            "icon": "Fill_Phials_2.png",
            "label": "Fill Phials Near",
            "action": charge_blade.fill_phials_2,
        },
        {
            "index": 8,
            "icon": "SAED_2.png",
            "label": "SAED 2",
            "action": charge_blade.saed_combo_2,
        },
        {
            "index": 9,
            "icon": "Savage_Axe_Finisher_2.png",
            "label": "S. Axe Combo",
            "action": charge_blade.savage_axe_combo,
        },
        {
            "index": 10,
            "icon": "Combo_1.png",
            "label": "Full Combo Far",
            "action": charge_blade.charge_blade_sword_combo,
        },
        {
            "index": 11,
            "icon": "Combo_2.png",
            "label": "Full Combo Near",
            "action": charge_blade.charge_blade_sword_combo_2,
        },
        {
            "index": 13,
            "icon": "SAED_1.png",
            "label": "SAED",
            "action": charge_blade.saed_combo,
        },
        {
            "index": 14,
            "icon": "Savage_Axe_Finisher_1.png",
            "label": "S. Axe Finisher",
            "action": charge_blade.savage_axe_finisher,
        },
    ]
