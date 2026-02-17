import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Moonpath brand colors
moonpath_bg_dark = '#2F2235'
moonpath_card_bg = '#3F3244'
moonpath_text = '#BFC3BA'
moonpath_accent = '#FFD1B3'
moonpath_green = '#6BBF6B'

# Create figure
fig, ax = plt.subplots(figsize=(12, 4))
fig.patch.set_facecolor(moonpath_bg_dark)
ax.set_facecolor(moonpath_bg_dark)
ax.set_xlim(0, 12)
ax.set_ylim(0, 4)
ax.axis('off')

# Card data
cards = [
    {
        'x': 0.5,
        'stat': '67.9%',
        'label': 'hit top 10 after grammy',
        'sublabel': '(up from 56.6%)'
    },
    {
        'x': 4.5,
        'stat': '2x more',
        'label': 'artists hit #1 after grammy',
        'sublabel': '(albums on billboard 200)'
    },
    {
        'x': 8.5,
        'stat': '53%',
        'label': 'improved or maintained',
        'sublabel': 'peak performance'
    }
]

# Draw cards
for card in cards:
    # Card background
    rect = patches.FancyBboxPatch(
        (card['x'], 0.5), 3, 3,
        boxstyle="round,pad=0.1",
        edgecolor=moonpath_accent,
        facecolor=moonpath_card_bg,
        linewidth=2,
        alpha=0.9
    )
    ax.add_patch(rect)
    
    # Big stat number (moved down slightly)
    ax.text(card['x'] + 1.5, 2.3, card['stat'],
            ha='center', va='center',
            color=moonpath_accent,
            fontsize=36,
            fontweight='bold')
    
    # Label (moved up to be closer to stat)
    ax.text(card['x'] + 1.5, 1.65, card['label'],
            ha='center', va='center',
            color=moonpath_text,
            fontsize=11,
            fontweight='normal')
    
    # Sublabel (green, BOLD, BIGGER) - stays at bottom
    ax.text(card['x'] + 1.5, 1.0, card['sublabel'],
            ha='center', va='center',
            color=moonpath_green,
            fontsize=12,  # Bigger than before (was 10)
            fontweight='bold',  # Now bold
            style='normal')  # Removed italic

# Title
fig.text(0.5, 0.95, 'the best new artist curse doesn\'t exist',
         ha='center', va='top',
         color=moonpath_accent,
         fontsize=18,
         fontweight='bold')

plt.tight_layout()
plt.savefig('grammy_curse_stat_cards.png', dpi=300, facecolor=moonpath_bg_dark,
            bbox_inches='tight', pad_inches=0.3)
plt.show()

print("✓ Chart saved: grammy_curse_stat_cards.png")
