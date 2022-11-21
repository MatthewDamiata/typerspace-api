import pytest
import ulid

from youtube_transcript_api import TranscriptsDisabled


@pytest.fixture()
def generate_random_youtube_id():
    # Must use a function here because fixtures are evaluated at import time
    def wrapper():
        return ulid.new().str[0:11]

    return wrapper


@pytest.fixture()
def validate_transcript():
    def wrapper(transcript):
        for caption in transcript:
            text = caption.get("text")
            assert caption.get("start")
            assert caption.get("duration")
            assert text
            assert chr(160) not in text
            assert "\n" not in text

    return wrapper


@pytest.fixture()
def mock_get_404_transcript():
    def wrapper(video_id):
        return None

    return wrapper


@pytest.fixture()
def mock_raise_transcripts_disabled():
    def wrapper(video_id):
        raise TranscriptsDisabled(video_id)

    return wrapper


@pytest.fixture()
def mock_get_transcript():
    def wrapper(video_id, languages=[]):
        return [
            {
                "text": "You were on your way home, when you died.",
                "start": 3.0,
                "duration": 2.72,
            },
            {"text": "It was a car accident.", "start": 6.1, "duration": 2.1},
            {
                "text": "Nothing particularly remarkable.",
                "start": 8.92,
                "duration": 2.28,
            },
            {"text": "But fatal, none the less.", "start": 11.48, "duration": 1.68},
            {"text": "It was a painless death.", "start": 13.74, "duration": 1.52},
            {
                "text": "The medics tried their best to save you... but to no avail.",
                "start": 15.46,
                "duration": 3.98,
            },
            {
                "text": "Your body was so utterly shattered, you were better off. Trust me.",
                "start": 19.9,
                "duration": 4.66,
            },
            {"text": "And that's when you met me.", "start": 25.335, "duration": 1.93},
            {"text": "What happened?", "start": 28.215, "duration": 1.19},
            {"text": "Where am I?", "start": 30.205, "duration": 1.05},
            {"text": "You died.", "start": 31.74, "duration": 0.879},
            {"text": "I said, matter of factly.", "start": 33.1, "duration": 1.792},
            {"text": "No point in mincing words.", "start": 35.26, "duration": 2.08},
            {
                "text": "There was... there was a truck.",
                "start": 37.6,
                "duration": 2.52,
            },
            {"text": "And it was skidding.", "start": 40.468, "duration": 1.272},
            {"text": "Yes.", "start": 43.14, "duration": 1.0},
            {"text": "I... I died?", "start": 44.58, "duration": 2.18},
            {"text": "Yes.", "start": 47.64, "duration": 0.78},
            {"text": "But don't feel bad about it.", "start": 49.0, "duration": 1.74},
            {"text": "Everyone dies.", "start": 51.4, "duration": 1.283},
            {"text": "You looked around.", "start": 53.12, "duration": 1.259},
            {"text": "There was... nothingness.", "start": 55.08, "duration": 1.78},
            {"text": "Just you, and me.", "start": 56.74, "duration": 2.28},
            {"text": "What is this place?", "start": 59.788, "duration": 1.292},
            {"text": "Is this, the afterlife?", "start": 62.255, "duration": 2.04},
            {"text": "More or less.", "start": 64.783, "duration": 1.217},
            {"text": "Are you... God?", "start": 67.0, "duration": 1.4},
            {"text": "Yes.", "start": 69.295, "duration": 0.625},
            {"text": "I'm God.", "start": 70.42, "duration": 0.755},
            {"text": "My kids...", "start": 72.7, "duration": 0.6},
            {"text": "My wife...", "start": 73.94, "duration": 0.92},
            {"text": "What about them?", "start": 75.94, "duration": 1.095},
            {"text": "Will they be alright?", "start": 78.34, "duration": 1.76},
            {
                "text": '"That\'s what I like to see," I said.',
                "start": 81.0,
                "duration": 2.269,
            },
            {
                "text": "You just died, and your main concern is for your family.",
                "start": 83.58,
                "duration": 3.648,
            },
            {
                "text": "That's good stuff right there.",
                "start": 87.228,
                "duration": 2.112,
            },
            {
                "text": "You looked at me with fascination.",
                "start": 90.408,
                "duration": 2.052,
            },
            {
                "text": "To you, I didn't look like God.",
                "start": 92.82,
                "duration": 2.609,
            },
            {
                "text": "I just looked like some man, or possibly a woman.",
                "start": 95.66,
                "duration": 3.188,
            },
            {
                "text": "Some vague authority figure maybe.",
                "start": 99.46,
                "duration": 1.96,
            },
            {"text": '"Don\'t worry," I said.', "start": 103.78, "duration": 0.98},
            {"text": "They'll be fine.", "start": 105.22, "duration": 0.88},
            {
                "text": "Your kids will remember you as perfect in every way.",
                "start": 106.46,
                "duration": 3.16,
            },
            {
                "text": "They didn't have time to grow contemptuous of you.",
                "start": 110.48,
                "duration": 2.88,
            },
            {
                "text": "Your wife will cry on the outside.",
                "start": 114.1,
                "duration": 2.24,
            },
            {"text": "But will be secretly relieved.", "start": 116.8, "duration": 1.7},
            {
                "text": "To be fair, your marriage was falling apart.",
                "start": 120.02,
                "duration": 2.82,
            },
            {
                "text": "If it's any consolation, she'll feel very guilty for feeling relieved.",
                "start": 123.6,
                "duration": 4.98,
            },
            {"text": "Oh...", "start": 129.56, "duration": 0.5},
            {"text": "So what happens now?", "start": 130.88, "duration": 1.28},
            {
                "text": "Do I go to Heaven? Or Hell or something?",
                "start": 133.02,
                "duration": 2.68,
            },
            {"text": "Neither.", "start": 136.88, "duration": 1.12},
            {"text": "You'll be reincarnated.", "start": 138.06, "duration": 1.54},
            {"text": "Ah...", "start": 140.96, "duration": 0.5},
            {"text": "So the Hindus were right!", "start": 142.92, "duration": 1.64},
            {
                "text": "All religions are right in their own way.",
                "start": 145.28,
                "duration": 2.06,
            },
            {"text": "Walk with me.", "start": 148.66, "duration": 0.66},
            {
                "text": "You followed along as we strolled through the void.",
                "start": 151.1,
                "duration": 2.82,
            },
            {"text": "Where are we going?", "start": 155.68, "duration": 0.76},
            {"text": "No where in particular.", "start": 157.28, "duration": 1.48},
            {
                "text": "It's just nice to walk while we talk.",
                "start": 158.78,
                "duration": 1.94,
            },
            {"text": "So, what's the point then?", "start": 162.24, "duration": 1.92},
            {
                "text": "When I get reborn, I'll just be a blank slate right?",
                "start": 165.22,
                "duration": 3.36,
            },
            {"text": "A baby?", "start": 169.76, "duration": 0.5},
            {
                "text": "So, all my experiences and everything... everything I did in this life...",
                "start": 171.14,
                "duration": 4.56,
            },
            {"text": "Won't matter...", "start": 176.04, "duration": 0.5},
            {"text": "Not so.", "start": 177.6, "duration": 0.82},
            {
                "text": "You have within you, all the knowledge and experiences of all your past lives.",
                "start": 179.14,
                "duration": 5.36,
            },
            {
                "text": "You just don't remember them right now.",
                "start": 185.0,
                "duration": 1.78,
            },
            {
                "text": "I stopped walking, and took you by the shoulders.",
                "start": 188.22,
                "duration": 2.78,
            },
            {
                "text": "Your soul is more magnificent, beautiful, and gigantic than you can possibly imagine.",
                "start": 191.64,
                "duration": 5.66,
            },
            {
                "text": "A human mind can only contain a tiny fraction of what you are.",
                "start": 198.52,
                "duration": 3.86,
            },
            {
                "text": "It's like sticking your finger in a glass of water.",
                "start": 203.22,
                "duration": 2.7,
            },
            {"text": "To see if it's hot or cold.", "start": 206.24, "duration": 1.28},
            {
                "text": "You put a tiny part of yourself into the vessel, and when you bring it back out, you've gained all the experiences it had.",  # noqa
                "start": 208.34,
                "duration": 7.54,
            },
            {
                "text": "You've been in a human for the last 48 years.",
                "start": 216.86,
                "duration": 2.64,
            },
            {
                "text": "So you haven't stretched out yet and felt the rest of your immense consciousness.",
                "start": 219.94,
                "duration": 4.42,
            },
            {
                "text": "If we hung out here for long enough, you'd start remembering everything.",
                "start": 225.46,
                "duration": 3.9,
            },
            {
                "text": "But there's not point to doing that between each life.",
                "start": 229.96,
                "duration": 2.32,
            },
            {
                "text": "How many times have I been reincarnated then?",
                "start": 234.06,
                "duration": 2.4,
            },
            {"text": "Oh, lots! Lots and lots!", "start": 237.8, "duration": 2.0},
            {
                "text": "And into lots of different lives.",
                "start": 240.22,
                "duration": 2.08,
            },
            {
                "text": "This time around, you'll be a Chinese peasant girl in 540 A.D.",
                "start": 242.76,
                "duration": 4.78,
            },
            {"text": "Wait... what?!", "start": 249.16, "duration": 1.46},
            {
                "text": "You're sending me back in time?",
                "start": 251.2,
                "duration": 1.78,
            },
            {"text": "Well I guess technically.", "start": 254.3, "duration": 1.74},
            {
                "text": "Time as you know it, only exists in your universe.",
                "start": 256.56,
                "duration": 3.34,
            },
            {
                "text": "Things are different where I come from.",
                "start": 260.5,
                "duration": 1.56,
            },
            {
                "text": "Where... where you come from?",
                "start": 263.56,
                "duration": 1.74,
            },
            {
                "text": "Oh sure, I come from somewhere. Somewhere else.",
                "start": 266.52,
                "duration": 3.1,
            },
            {
                "text": "And there are others like me.",
                "start": 270.04,
                "duration": 1.76,
            },
            {
                "text": "I know you'll want to know what it's like there but honestly you wouldn't understand.",
                "start": 272.44,
                "duration": 4.26,
            },
            {"text": '"Oh..."', "start": 278.4, "duration": 0.5},
            {"text": "You said, a little let down.", "start": 279.2, "duration": 1.58},
            {"text": "But wait...", "start": 281.92, "duration": 0.54},
            {
                "text": "If I get reincarnated to other places in time, I could have interacted with myself at some point.",  # noqa
                "start": 283.24,
                "duration": 5.98,
            },
            {"text": "Sure, happens all the time.", "start": 291.0, "duration": 1.74},
            {
                "text": "And with both lives only aware of their own lifespans, you don't even know it's happening.",
                "start": 293.24,
                "duration": 5.48,
            },
            {"text": "So...", "start": 300.18, "duration": 0.74},
            {"text": "what's the point of it all?", "start": 300.92, "duration": 1.663},
            {"text": "I looked you in the eye.", "start": 303.403, "duration": 1.277},
            {"text": "The meaning of life,", "start": 305.2, "duration": 1.711},
            {
                "text": "the reason I made this whole universe,",
                "start": 306.911,
                "duration": 2.489,
            },
            {"text": "is for you to mature.", "start": 309.4, "duration": 2.0},
            {"text": "You mean... mankind?", "start": 312.0, "duration": 1.86},
            {"text": "You want to us to mature?", "start": 313.86, "duration": 2.0},
            {"text": "No, just you.", "start": 317.02, "duration": 1.24},
            {
                "text": "I made this whole universe for you.",
                "start": 318.76,
                "duration": 2.128,
            },
            {"text": "With each new life", "start": 321.22, "duration": 1.38},
            {
                "text": "you grow and mature, and become a larger and greater intellect.",
                "start": 322.6,
                "duration": 4.1,
            },
            {"text": "Just me?", "start": 328.1, "duration": 0.9},
            {"text": "What about everyone else?", "start": 329.54, "duration": 1.7},
            {"text": "There is no one else.", "start": 332.08, "duration": 1.52},
            {
                "text": "In this universe, there's just you and me.",
                "start": 333.6,
                "duration": 3.531,
            },
            {"text": "You stared blankly at me.", "start": 337.94, "duration": 1.751},
            {
                "text": "But all the people on Earth...",
                "start": 340.5,
                "duration": 1.406,
            },
            {"text": "All you.", "start": 342.48, "duration": 1.031},
            {
                "text": "Different incarnations of you.",
                "start": 343.68,
                "duration": 2.092,
            },
            {"text": "Wait... I'm... everyone?", "start": 346.7, "duration": 2.56},
            {"text": "Now you're getting it.", "start": 350.32, "duration": 1.64},
            {
                "text": "I'm every human being who ever lived?",
                "start": 352.56,
                "duration": 2.394,
            },
            {"text": "Or who will ever live,  yes.", "start": 356.56, "duration": 2.56},
            {"text": "I'm Abraham Lincoln?", "start": 359.7, "duration": 1.26},
            {
                "text": "And you're John Wilkes Booth too.",
                "start": 362.04,
                "duration": 2.16,
            },
            {"text": "I'm Hitler?!", "start": 364.6, "duration": 1.18},
            {"text": "You said appalled.", "start": 366.589, "duration": 1.577},
            {
                "text": "And you're the millions he killed.",
                "start": 368.8,
                "duration": 2.08,
            },
            {"text": "I'm Jesus?!", "start": 371.18, "duration": 1.7},
            {
                "text": "And you're everyone who followed Him.",
                "start": 373.08,
                "duration": 2.1,
            },
            {"text": "You fell silent.", "start": 375.7, "duration": 1.56},
            {
                "text": "Every time you victimized someone, you were victimizing yourself.",
                "start": 378.2,
                "duration": 3.891,
            },
            {
                "text": "Every act of kindness you have done, you have done to yourself.",
                "start": 382.64,
                "duration": 4.1,
            },
            {
                "text": "Every happy and sad moment ever experienced by any human was or will be experienced by you.",
                "start": 387.0,
                "duration": 7.86,
            },
            {"text": "You thought for a long time.", "start": 396.02, "duration": 1.66},
            {"text": "Why? Why do all this?", "start": 398.88, "duration": 3.44},
            {
                "text": "Because someday you will become like me.",
                "start": 402.38,
                "duration": 3.151,
            },
            {
                "text": "Because that's what you are!",
                "start": 405.66,
                "duration": 2.218,
            },
            {"text": "You're one of my kind.", "start": 407.878, "duration": 2.042},
            {"text": "You're my child!", "start": 409.92, "duration": 1.58},
            {"text": "Wow!! You said incredulous.", "start": 413.1, "duration": 2.24},
            {"text": "You mean I'm a God?", "start": 415.72, "duration": 1.84},
            {
                "text": "No, not yet, you're a fetus.",
                "start": 419.04,
                "duration": 2.623,
            },
            {"text": "You're still growing.", "start": 421.663, "duration": 1.317},
            {
                "text": "Once you've lived every human life throughout all time,",
                "start": 423.14,
                "duration": 3.872,
            },
            {
                "text": "you will have grown enough to be born.",
                "start": 427.012,
                "duration": 2.548,
            },
            {"text": "So the whole universe...", "start": 430.98, "duration": 1.82},
            {"text": "it's just...", "start": 433.3, "duration": 1.18},
            {"text": "an egg!", "start": 435.28, "duration": 0.931},
            {"text": "I answered:", "start": 436.46, "duration": 1.4},
            {
                "text": "now it's time for you to move on to your next life.",
                "start": 438.12,
                "duration": 2.669,
            },
            {"text": "And I sent you on your way.", "start": 441.32, "duration": 1.747},
        ]

    return wrapper
