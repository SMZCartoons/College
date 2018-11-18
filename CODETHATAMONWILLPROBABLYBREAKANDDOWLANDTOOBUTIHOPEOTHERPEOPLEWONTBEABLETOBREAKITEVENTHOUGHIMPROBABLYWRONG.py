Numbers1 = [13, 26, 14, 25, 15, 24, 16, 23, 17, 22, 18, 21, 19, 20, 13, 1, 11, 2, 10, 3, 9, 4, 8, 5, 6, 7]
Combined_Letters = ["ML", "LK", "KJ", "JI", "IH", "HG", "GF", "FE", "ED", "DC", "CB", "BA", "AN", "NO", "OP", "PQ", "QR", "RS", "ST", "TU","UV","VW", "WX", "XY", "YZ", "ZA"]
Numbers2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52] and ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W" "X", "Y", "Z", " "]

def unbreakable (input):
    return Numbers1[Alphabet.index(input)]
def breakable (input):
    return Alphabet[Numbers1.index(input)]


text = str.upper(input("Type in your text"))
question = input("Encrypt or Decrypt?")
if(question == "Encrypt"):
    for letter in text:
        print(unbreakable(letter), end="")
if(question == "Decrypt"):
    for letter in text.split(" "):
        print(breakable(int(letter)), end="")
    
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=EDGE">
    <title>Run, Bucket, Run</title>
    <script src="https://bitbucket.org/atlassian-connect/all.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/superagent/1.2.0/superagent.min.js"></script>
    <style>
      canvas {
        cursor: pointer;
      }
    </style>
  </head> 
  <body>

  <!-- All audio courtesy of Matt Pettersen -->
  <script>
    ["theme",
      "fall",
      "jump",
      "win"
    ].forEach(function(file) {
              var audioEl = document.createElement('audio');
              audioEl.id = file;
              audioEl.src = "https://s3-us-west-1.amazonaws.com/" +
                      "run-bucket-run/rbr-" + file + ".mp3";
              audioEl.preload = "auto";
              document.querySelector("body").appendChild(audioEl);
            });
  </script>

    <div id="page">    
      <section id="content" role="main">        
        <canvas id="viewport" width="1000" height="500"></canvas>
      </section>
    </div>

    <script>
      // constants
      var PHYSICS = {
        INITIAL_VX: 0,
        MAX_VX: .28,
        AX: 0.0000025,
        JUMP_A: .003,
        JUMP_MAX: .3,
        RUN_A: .5,
        RUN_MAX: .315,
        GRAVITY: .001,
        FRICTION: .05,
        TILT_MAX: .2,
        TILT_RATE: .001,
        PLATFORM_SPEED_MAX: .15,
        PLATFORM_JUMP_PROXIMITY: 5
      }, DIM = {
        HEAD_ROOM: 100,
        SCORE_YPOS: 40,
        PLATFORM_GAP_MIN: 50,
        PLATFORM_GAP_MAX: 150,
        PLATFORM_WIDTH_MIN: 50,
        PLATFORM_WIDTH_MAX: 225,        
        PLATFORM_MOVE_MIN: 100,
        PLATFORM_MOVE_MAX: 250,
        PLATFORMS_MOVE_AFTER: 30,
        PLATFORM_MOVER_CHANCE: .45,
        MAX_PLATFORM_VDIFF: 65,
        PLATFORM_FONT: "24px serif",
        FONT_HEIGHT: 24,
        FONT_YOFFSET: 4
      }, COLOUR = {
        PLATFORM: "#cccccc",
        PLATFORM_TEXT: "#205081"
      }, TIME = {
        DEATH_DELAY: 1500,
        MAX_FRAME_DELAY: 200,
        TIME_WARP: 1
      }, AUDIO = {
        MUSIC: document.querySelector("#theme"),
        JUMP: document.querySelector("#jump"),
        DEATH: document.querySelector("#fall"),
        WIN: document.querySelector("#win")
      }, SCORE = {
        MULTIPLIER_MIN: .01,
        MULTIPLIER_MAX: 5,
        MULTIPLIER_A: .00003
      };

      AUDIO.MUSIC.loop = true;

      var canvas = document.getElementById('viewport');
      var ctx = canvas.getContext('2d');
      var avatar = {};
      var imagesLoading = 0;
      var soundOn = true;

      var RBR = {
        formatScoreText: function(score) {
          var scoreText = Math.floor(score).toString(16);
          if (score.length > 8) {
            scoreText = "OVERFLOW!";
          } else {
            while (scoreText.length < 8) scoreText = "0" + scoreText;
            scoreText = "0x" + scoreText;
          }
          return scoreText;
        },
        fillCenteredText: function(text, yOffsetFromCenter) {
          var x = (canvas.width - ctx.measureText(text).width) / 2;
          var y = canvas.height / 2 + yOffsetFromCenter;
          ctx.fillText(text, x, y);
          return {x: x, y: y};
        },
        clearCanvas: function() {
          ctx.clearRect(0, 0, canvas.width, canvas.height);
        },
        queryParam: function(name) {
          var matches = location.search.match(new RegExp('[\?&]' + name + '=([^\&]*)'));
          return matches && decodeURIComponent(matches[1]);
        },
        inIframe: function() {
          try {
            return window.self !== window.top;
          } catch (e) {
            return true;
          }
        },
        requiresAuthentication: function(repoUuid) {
          // whitelist of repos to access via CORS rather than AP.request
          return [
            // kannonboy/run-bucket-run
            "{3b49d567-0263-4e0f-9d04-56ca2114e72d}",
            // tpettersen/run-bucket-run
            "{cef978c8-9a80-4cfa-871f-5896c9a83a5a}"
          ].indexOf(repoUuid) === -1;
        },
        loadImage: function(url) {
          var image = new Image();
          image.src = url;
          imagesLoading++;
          image.onload = function() {
            imagesLoading--;
          };
          return image;
        },
        isImagesLoading: function() {
          return imagesLoading > 0;
        },
        resetCurrentTime: function(audio) {
          // work around HTML5 audio InvalidStateError in some browsers
          if (audio.currentTime !== 0) audio.currentTime = 0;
        },
        tryCatchIgnore: function(fn) {
          // for working around SecurityExceptions
          // thrown due to browser cookie settings
          try {
            fn();
          } catch (e) {
            // ignore
          }
        },
        isDemoMode: function() {
          var demo = RBR.queryParam("demo") && true;
          RBR.isDemoMode = function() {
            return demo;
          };
          return demo;
        }
      };

      var IMAGE = {
        BUCKET: RBR.loadImage("bitbucket.png"),
        TWITTER: RBR.loadImage("twitter.png"),
        WRENCH: RBR.loadImage("wrench.png"),
        VOLUME_ON: RBR.loadImage("volume_on.png"),
        VOLUME_OFF: RBR.loadImage("volume_off.png")
      };

      var customWidth = RBR.queryParam("width"),
          customHeight = RBR.queryParam("height");

      if (customWidth) {
        canvas.width = customWidth;
      }
      if (customHeight) {
        canvas.height = customHeight;
      }

      // store high score by repo, commit & path
      var scoreKey = "highScore$" + RBR.queryParam('repo') +
                     '$' + RBR.queryParam('cset') +
                     '$' + RBR.queryParam('path');

      function createPlatforms(src) {

        // need to set font to calculate platform dimensions
        ctx.font = DIM.PLATFORM_FONT;

        // split the source by newline
        // and calculate their indent
        var maxIndent = 0;
        var lines = src
                .split("\n")
                .map(function(line) {
                  var indent = line.match(/^\s*/)[0].length;
                  maxIndent = Math.max(indent, maxIndent);
                  return {
                    indent: indent,
                    text: line.trim()
                  };
                }).filter(function(line) {
                  // filter out blank lines
                  return line.text.length > 0;
                });

        // a max indent of < 10 will make many jumps impossible
        maxIndent = Math.max(maxIndent, 10);

        var prev = {x:0, width:0, moveDistance:0};

        return lines.map(function(line, index) {
          // non-zero moveDistance indicates a moving platform
          var moveDistance = 0;
          var width = ctx.measureText(line.text).width;

          // randomly select some platforms as "movers", provided
          // it's within certain size limits and the previous one
          // isn't a mover
          if (!prev.moveDistance &&
              index > DIM.PLATFORMS_MOVE_AFTER &&
              width > DIM.PLATFORM_WIDTH_MIN &&
              width < DIM.PLATFORM_WIDTH_MAX &&
              Math.random() < DIM.PLATFORM_MOVER_CHANCE) {
            moveDistance = DIM.PLATFORM_MOVE_MIN + 
                           Math.random() * (DIM.PLATFORM_MOVE_MAX - DIM.PLATFORM_MOVE_MIN);
          }

          // calculate a random gap between platforms, gaps
          // adjacent to moving platforms are slightly smaller
          var x = prev.x + prev.width + prev.moveDistance +
                  DIM.PLATFORM_GAP_MIN +
                  (moveDistance || prev.moveDistance ? 0.66 : 1) * 
                  Math.random() * (DIM.PLATFORM_GAP_MAX - DIM.PLATFORM_GAP_MIN);
                  
          // platform elevation is based on indent
          var y = DIM.HEAD_ROOM + (1 - line.indent / maxIndent) *
                  (canvas.height - 2 * DIM.HEAD_ROOM);

          // make sure the jump is possible
          if (prev.y - y > DIM.MAX_PLATFORM_VDIFF) {
            y = prev.y - DIM.MAX_PLATFORM_VDIFF;
          }

          // and here's what what we need to render a platform
          return prev = {
            x: x,
            y: y,
            originX: x,
            originY: y,
            moveDistance: moveDistance,
            // -1 == left, 0 == stopped, 1 == right
            moving: moveDistance ? 1 : 0,
            width: width,
            height: DIM.FONT_HEIGHT,
            text: line.text
          };
        });
      }

      // cache the last left/right keydown, as we only want to zero out
      // horizontal velocity when the most recently pressed left/right keyup
      // event is triggered
      var lastXKeyDown = null;

      // bind keys
      document.onkeydown = function(e) {
        var trapKeyEvent = true;
        switch (e.keyCode) {
          case 37: // left
          case 65: // a
            avatar.running = -1;
            lastXKeyDown = e.keyCode;
            break;
          case 32: // space
          case 38: // up
          case 87: // w
            // JUMP! (if on a platform or close enough to one)
            if (avatar.platform ||
                    (avatar.platformBelow &&
                     avatar.platformBelow.y - avatar.y < PHYSICS.PLATFORM_JUMP_PROXIMITY)) {
              avatar.jumping = true;              
              RBR.resetCurrentTime(AUDIO.JUMP); // seek to beginning of sfx
              AUDIO.JUMP.play();
            }
            break;
          case 39: // right
          case 68: // d
            avatar.running = 1;
            lastXKeyDown = e.keyCode;
            break;
          case 40: // down
            break;
          default:
            trapKeyEvent = false;
        }

        // prevent arrow key from scrolling window
        if (trapKeyEvent) {
          if (e.preventDefault) {
            e.preventDefault();
          }
          e.returnValue = false;
        }        
      };

      document.onkeypress = function(e) {
        switch (e.keyCode) {
          case 33: // !
            var demoMode = !RBR.isDemoMode();
            RBR.isDemoMode = function() {
              return demoMode;
            };
            // massive hack - this kills the player
            avatar.y = canvas.height * 2;
            break;
        }
      };

      document.onkeyup = function(e) {
        switch (e.keyCode) {
          case 37: // left
          case 39: // right
          case 65: // a
          case 68: // d
            if (e.keyCode === lastXKeyDown) {
              avatar.running = 0;
              lastXKeyDown = null;
            }
            break;
          case 32: // space
          case 38: // up
          case 87: // w
            avatar.jumping = false;
            break;
        }
      };

      function reinitGame(src, skipSplash) {
        skipSplash = skipSplash || RBR.isDemoMode();

        AUDIO.MUSIC.volume = soundOn ? .5 : 0;
        RBR.resetCurrentTime(AUDIO.MUSIC);

        var platforms = createPlatforms(src);

        var firstPlatform = platforms[0];
        var finalPlatform = platforms[platforms.length - 1];

        var startX = firstPlatform.x + firstPlatform.width / 2;
        var finishX = finalPlatform.x + finalPlatform.width + 5;

        // our hero, bucket
        avatar = {
          x: startX,
          y: firstPlatform.y,
          vx: 0,
          vy: 0,
          rotation: 0,
          // true == forward, false == back
          tilt: true,
          // -1 == left, 0 == stopped, 1 == right
          running: 0
        };

        var scrollOffset = 0;
        var scrollVelocity = PHYSICS.INITIAL_VX;
        var score = 0;
        var scoreMultiplier = SCORE.MULTIPLIER_MIN;
        var maxAvatarX = startX;

        // the further right we go,
        // the faster the screen scrolls
        function scrollScreen(elapsed) {
          scrollVelocity = Math.min(scrollVelocity + PHYSICS.AX * elapsed, PHYSICS.MAX_VX);
          scrollOffset = Math.max(scrollOffset + scrollVelocity * elapsed, avatar.x - 2 * canvas.width / 3);
          if (avatar.running) {
            scoreMultiplier += SCORE.MULTIPLIER_A * elapsed;
            scoreMultiplier = Math.min(SCORE.MULTIPLIER_MAX, scoreMultiplier);
          } else {
            scoreMultiplier = SCORE.MULTIPLIER_MIN;
          }
          score += Math.max(avatar.x - maxAvatarX, 0) * scoreMultiplier;
          maxAvatarX = Math.max(avatar.x, maxAvatarX);
        }

        // draw our hero
        function renderBucket() {
          ctx.save();
          // have to do some translation here to
          // rotate the bucket around its center
          ctx.translate(avatar.x - scrollOffset - IMAGE.BUCKET.width / 2, avatar.y - IMAGE.BUCKET.height);
          // TODO why translate twice?
          ctx.translate(IMAGE.BUCKET.width / 2, IMAGE.BUCKET.height / 2);
          ctx.rotate(avatar.rotation);
          ctx.drawImage(IMAGE.BUCKET, -IMAGE.BUCKET.width / 2, -IMAGE.BUCKET.height / 2);
          ctx.restore();
        }

        function renderScore() {
          ctx.font = "36px monospace";
          var scoreText = RBR.formatScoreText(score);
          var scoreWidth = ctx.measureText(scoreText).width;
          ctx.fillText(scoreText, (canvas.width - scoreWidth) / 2, DIM.SCORE_YPOS);
        }

        function renderVolumeControl() {
          var soundIcon = soundOn ? IMAGE.VOLUME_ON : IMAGE.VOLUME_OFF;
          ctx.drawImage(soundIcon, canvas.width - 30 - soundIcon.width, 10);
        }

        function renderPlatforms() {
          ctx.font = DIM.PLATFORM_FONT;
          for (var i = 0; i < platforms.length; i++) {
            var platform = platforms[i];
            if (platform.x - scrollOffset > canvas.width) {
              // we're off screen right, stop rendering
              break;
            }
            ctx.fillStyle = COLOUR.PLATFORM;
            // for debugging demo mode
            // if (platform === DEMO.targetPlatform) {
            // ctx.fillStyle = "#ff0000";
            // }
            ctx.beginPath();
            ctx.rect(platform.x - scrollOffset, platform.y + DIM.FONT_YOFFSET, platform.width, platform.height);
            ctx.closePath();
            ctx.fill();
            ctx.fillStyle = COLOUR.PLATFORM_TEXT;       
            ctx.fillText(platform.text, platform.x - scrollOffset, platform.y + platform.height);
          }
        }

        // platform speed is relative to
        // the current side-scroll speed
        function platformSpeed() {
          return (1.15 * scrollVelocity / PHYSICS.MAX_VX) * PHYSICS.PLATFORM_SPEED_MAX;
        }

        function updatePlatforms(elapsed) {
          for (var i = 0; i < platforms.length; i++) {
            var platform = platforms[i];
            if (platform.x - scrollOffset + platform.width < 0) {
              // dispose of platforms once they're off screen left
              platforms.shift();
              i--;
              continue;
            }
            if (platform.x - scrollOffset > canvas.width * 2) {
              // don't bother updating platforms over a
              // whole screen width to the right
              break;
            }            

            if (platform.moving === 1) {
              if (platform.x > platform.originX + platform.moveDistance) {
                platform.moving = -1;
              } else {
                platform.x += elapsed * platformSpeed();
              }
            } else if (platform.moving === -1) {
              if (platform.x < platform.originX) {
                platform.moving = 1;
              } else {
                platform.x -= elapsed * platformSpeed();
              }
            }

          }          
        }

        function updatePhysics(elapsed) {
          avatar.vy += PHYSICS.GRAVITY * elapsed;
          avatar.falling = true;
          // cache platforms for demo mode
          avatar.platform = null;
          avatar.platformBelow = null;
          avatar.nextPlatform = null;
          avatar.nextNextPlatform = null;
          var avatarLeft = avatar.x - IMAGE.BUCKET.width / 2;
          var avatarRight = avatar.x + IMAGE.BUCKET.width / 2;

          var platformVx = 0;

          // in this loop we try to find the platform
          // our hero bucket is standing on
          for (var i = 0; i < platforms.length; i++) {
            var platform = platforms[i];
            // platform is too far right
            if (platform.x > avatarRight) {
              // TODO this is pretty lazy
              if (avatar.nextPlatform) {
                avatar.nextNextPlatform = platform;
                break;
              } else {
                avatar.nextPlatform = platform;
                continue;
              }
            }
            // platform is too far left OR above our hero
            if (platform.x + platform.width < avatarLeft) continue;
            // platform is above our hero
            if (platform.y < avatar.y) continue;
            // out hero is on the platform!
            if (platform.y - avatar.y <= Math.max(1, avatar.vy * elapsed)) {
              avatar.falling = false;
              avatar.platform = platform;
              // if the platform is moving, we must
              // add its velocity to our hero
              if (platform.moveDistance) {
                platformVx = platform.moving * platformSpeed();
              }
            } else {
              avatar.platformBelow = platform;
            }
            // don't exit loop if we've found a platform, need
            // cache the next two platforms too
          }
          
          // if we're not falling, we can't be going down
          if (!avatar.falling) {
            avatar.vy = Math.min(0, avatar.vy);
          }

          // if we're jumping, accelerate upwards
          if (avatar.jumping) {
            avatar.vy -= PHYSICS.JUMP_A * elapsed;
            if (avatar.vy <= -PHYSICS.JUMP_MAX) {
              avatar.vy = -PHYSICS.JUMP_MAX;
              avatar.jumping = false;
            }
          }

          if (avatar.running === -1) {
            // running left
            avatar.vx = Math.max(avatar.vx - PHYSICS.RUN_A * elapsed, -PHYSICS.RUN_MAX);
          } else if (avatar.running === 1) {
            // running right
            avatar.vx = Math.min(avatar.vx + PHYSICS.RUN_A * elapsed, PHYSICS.RUN_MAX);
          } else if (avatar.vx < 0) {
            // momentum left
            avatar.vx = Math.min(avatar.vx + PHYSICS.FRICTION * elapsed, 0);
          } else if (avatar.vx > 0) {
            // momentum right
            avatar.vx = Math.max(avatar.vx - PHYSICS.FRICTION * elapsed, 0);
          }

          // displace avatar based on velocity
          avatar.x += (platformVx + avatar.vx) * elapsed;
          avatar.y += avatar.vy * elapsed;          
        }
        
        // figuring out what angle the bucket is at
        // is purely cosmetic, but kinda complex
        function updateBucketRotation(elapsed) {
          var tiltRotation = PHYSICS.TILT_RATE * elapsed;

          if (avatar.x > finishX) {
            // dramatic winning flip!
            AUDIO.MUSIC.pause();
            AUDIO.WIN.play();
            avatar.rotation += .1;
          } else if (avatar.falling) {
            // if we're falling, tilt towards the
            // direction of travel
            // TODO DRY this up
            if (avatar.running > 0) {
              if (avatar.vy > -.1) {
                avatar.rotation = Math.min(PHYSICS.TILT_MAX, avatar.rotation + tiltRotation);
              } else {
                avatar.rotation = Math.max(-PHYSICS.TILT_MAX, avatar.rotation - tiltRotation);
              }
            } else {
              if (avatar.vy < -.1) {
                avatar.rotation = Math.min(PHYSICS.TILT_MAX, avatar.rotation + tiltRotation);
              } else {
                avatar.rotation = Math.max(-PHYSICS.TILT_MAX, avatar.rotation - tiltRotation);
              }
            }
          } else if (avatar.running) {
            // rock the bucket forward and back while running
            if (avatar.tilt) {
              // tilting forward
              avatar.rotation += tiltRotation;
              if (avatar.rotation > PHYSICS.TILT_MAX / 2) {
                avatar.rotation = PHYSICS.TILT_MAX / 2;
                if (!avatar.falling) avatar.tilt = false;
              }
            } else {
              // tilting back
              avatar.rotation -= tiltRotation;
              if (avatar.rotation < -PHYSICS.TILT_MAX / 2) {
                avatar.rotation = -PHYSICS.TILT_MAX / 2;
                if (!avatar.falling) avatar.tilt = true;
              }
            }
          } else {
            // rock the bucket back to center when stationary
            if (avatar.rotation > 0) {
              avatar.rotation = Math.max(avatar.rotation - tiltRotation * 2, 0);
            } else {
              avatar.rotation = Math.min(avatar.rotation + tiltRotation * 2, 0);
            }
          }
        }

        function checkDead() {
          // the floor is lava
          if (avatar.y < canvas.height) {
            return false;
          }

          // you didn't make it pal, no victory music
          if (avatar.x < finishX) {
            AUDIO.MUSIC.pause();
            AUDIO.DEATH.play();
          }

          score = Math.floor(score);

          RBR.tryCatchIgnore(function() {
            // no localStorage? no high score for you
            if (window.localStorage) {
              var storedScore = localStorage.getItem(scoreKey);
              if (!storedScore || score > storedScore) {
                localStorage.setItem(scoreKey, score);
              }
            }
          });

          // a short delay to meditate on the frivolity of life
          setTimeout(function() {
            RBR.clearCanvas();
            if (RBR.isDemoMode()) {
              reinitGame(src);
            } else {
              renderEndScreen(score);
            }
          }, TIME.DEATH_DELAY);

          return true;
        }

        var DEMO = {
          nextJumpX: null,
          prevPlatform: null,
          targetPlatform: null,
          MIN_JUMP_VY: -.16,
          MIN_HORIZONTAL_JUMP: 150,
          MAX_HORIZONTAL_JUMP: 270,
          PLATFORM_LIP: 50,
          CAUTIOUS_MOVE_DISTANCE: 190
        };

        // AI for demo mode
        function playDemoBucket() {
          if (!avatar.nextPlatform) {
            // we're at the end of the level, JUMP!
            avatar.jumping = avatar.platform && avatar.x > avatar.platform.x + avatar.platform.width - DEMO.PLATFORM_LIP;
            avatar.running = 1;
            return;
          }

          if (avatar.platform && !avatar.jumping) {
            // we're on a platform
            // keep running, unless the platform we're
            // on is moving and we're close to the edge
            avatar.running = avatar.platform.moving &&
                             avatar.x > avatar.platform.x + avatar.platform.width - DEMO.PLATFORM_LIP
                             ? 0 : 1;
            DEMO.prevPlatform = avatar.platform;
            if (!DEMO.nextJumpX) {
              // calculate Bucket's next jump
              if (avatar.platform.moving) {
                // if we're moving, pick a point in space
                // we can definitely make the jump from
                DEMO.nextJumpX = avatar.nextPlatform.x - DEMO.MAX_HORIZONTAL_JUMP + DEMO.PLATFORM_LIP;
              } else {
                // otherwise just jump from near the end
                // of the platform
                DEMO.nextJumpX = Math.max(avatar.x, avatar.platform.x + avatar.platform.width - Math.random() * DEMO.PLATFORM_LIP);
              }
              if (avatar.nextNextPlatform &&
                  avatar.nextNextPlatform.x < DEMO.nextJumpX + DEMO.MAX_HORIZONTAL_JUMP &&
                  avatar.nextNextPlatform.y >= DEMO.prevPlatform.y &&
                  !avatar.nextNextPlatform.moving) {
                // we can jump right over the next platform!
                DEMO.targetPlatform = avatar.nextNextPlatform;
              } else {
                // just jump to the next platform
                DEMO.targetPlatform = avatar.nextPlatform;
              }
            }
            if (DEMO.nextJumpX && avatar.x >= DEMO.nextJumpX) {
              // we're passed the jump spot we picked, JUMP!
              if (DEMO.targetPlatform.moveDistance > DEMO.CAUTIOUS_MOVE_DISTANCE &&
                    (DEMO.targetPlatform.moving === 1 ||
                     DEMO.targetPlatform.x > DEMO.targetPlatform.originX + DEMO.targetPlatform.moveDistance / 2)) {
                // shit, the next platform moves a long way
                // better wait 'til it's real close
                avatar.running = 0;
              } else {
                // JUMP!
                // TODO encapsulate the jump SFX properly
                RBR.resetCurrentTime(AUDIO.JUMP); // seek to beginning of sfx
                AUDIO.JUMP.play();
                avatar.running = 1;
                avatar.jumping = true;
                DEMO.nextJumpX = null;
              }
            } else {
              // we're not at the jump point yet, keep running
              avatar.jumping = false;
            }
          } else {
            if (avatar.jumping &&
                    avatar.vy < DEMO.MIN_JUMP_VY &&
                    !DEMO.targetPlatform.moving &&
                    DEMO.targetPlatform.x - avatar.x < DEMO.MIN_HORIZONTAL_JUMP &&
                    DEMO.targetPlatform.y >= DEMO.prevPlatform.y) {
              // if the next platform is close, we just do a small jump
              avatar.jumping = false;
            }

            if (avatar.platformBelow === DEMO.targetPlatform) {
              // if we're over the target platform, let go of the jump button
              avatar.jumping = false;
              if (avatar.platformBelow.x + avatar.platformBelow.width - avatar.x < IMAGE.BUCKET.width / 2) {
                // if we're getting close to the end of the platform, just drop
                avatar.running = 0;
              }
            }
          }
        }

        function renderSplash() {
          ctx.drawImage(IMAGE.BUCKET, (canvas.width - IMAGE.BUCKET.width) / 2, canvas.height / 2 - 40);
          ctx.fillStyle = COLOUR.PLATFORM_TEXT;
          ctx.font = "48px monospace";
          RBR.fillCenteredText("Run, Bucket, Run!", -75);
          ctx.font = "36px monospace";
          RBR.fillCenteredText("a Bitbucket add-on", 80);
          ctx.font = "24px monospace";
          RBR.fillCenteredText("(click to play)", 120);

          RBR.tryCatchIgnore(function() {
            if (window.localStorage) {
              var highScore = localStorage.getItem(scoreKey);
              if (highScore) {
                RBR.fillCenteredText("High score: " + RBR.formatScoreText(highScore), -150);
              }
            }
          });

          document.documentElement.onclick = startGame;
        }

        function renderEndScreen(score) {

          ctx.fillStyle = COLOUR.PLATFORM_TEXT;
          ctx.font = "48px monospace";

          var highScore = score;
          RBR.tryCatchIgnore(function() {
            if (window.localStorage) {
              highScore = localStorage.getItem(scoreKey);
            }
          });
          RBR.fillCenteredText("High score: " + RBR.formatScoreText(highScore), -160);

          ctx.font = "40px monospace";

          var tweetXY = RBR.fillCenteredText("Tweet this!", -55);
          ctx.drawImage(IMAGE.TWITTER,
                          tweetXY.x - IMAGE.TWITTER.width - 25,
                          tweetXY.y - 15 - IMAGE.TWITTER.height / 2);
          var bucketText = "Play again";
          var bucketXY = RBR.fillCenteredText(bucketText, 45);
          ctx.drawImage(IMAGE.BUCKET,
                          bucketXY.x - IMAGE.BUCKET.width - 25,
                          bucketXY.y - 15 - IMAGE.BUCKET.height / 2);
          var wrenchXY = RBR.fillCenteredText("Under the hood", 145);
          ctx.drawImage(IMAGE.WRENCH,
                          wrenchXY.x - IMAGE.WRENCH.width - 25,
                          wrenchXY.y - 15 - IMAGE.WRENCH.height / 2);

          document.documentElement.onclick = function (event) {

            var offsetX = event.offsetX || event.pageX;
            var offsetY = event.offsetY || event.pageY;

            if (offsetX !== undefined &&
                offsetY !== undefined) {
              // did they click the tweet this button?
              if (offsetY > tweetXY.y - 50 &&
                  offsetY < tweetXY.y + 20) {
                // scumbag viral marketing tactics
                var filename = RBR.queryParam("name");
                window.open("https://twitter.com/intent/tweet?text=" +
                        "I%20scored%20" + RBR.formatScoreText(highScore) +
                        (filename && filename.length < 45 ? "%20on%20" + filename : "") +
                        "%20in%20Run,%20Bucket,%20Run!%20Play%20at" +
                        "%20https%3A%2F%2Fbitbucket.org%2F" +
                        "tpettersen%2Frun-bucket-run%2Fsrc%2F" +
                        "master%2Fgame.html%3Fat%3Dmaster%26" +
                        "fileviewer%3Drun-bucket-run%253Agame%20" +
                        "%23RunBucketRun",
                        "NewTweetWindow");
                return;
              // did they click the wrench button?
              } else if (offsetY > wrenchXY.y - 50 &&
                         offsetY < wrenchXY.y + 20) {
                window.open("https://developer.atlassian.com/blog/2015/10/bitbucket-fileview-addon/");
                return;
              }
            }

            reinitGame(src, true);
          };

        }

        // the eternal game loop, each function
        // is passed the elapsed time in ms
        var pipeline = [
          RBR.clearCanvas,
          scrollScreen,          
          updatePhysics,
          updatePlatforms,
          updateBucketRotation,
          renderPlatforms,
          renderBucket,
          renderScore,
          renderVolumeControl
        ];

        if (RBR.isDemoMode()) {
          pipeline.push(playDemoBucket);
        }

        var timeWarp = RBR.queryParam("warp") || TIME.TIME_WARP;

        var lastTimestamp;        
        function animate(now) {

          if (lastTimestamp) {
            var elapsed = Math.min(TIME.MAX_FRAME_DELAY, now - lastTimestamp);
            elapsed *= timeWarp;
            pipeline.forEach(function (fn) {
              fn(elapsed);
            });
          }
          lastTimestamp = now;

          if (checkDead()) {
            return;
          }

          window.requestAnimationFrame(animate);
        }

        function startGame() {
          window.requestAnimationFrame(animate);
          AUDIO.MUSIC.play();

          // wire up sound button
          document.documentElement.onclick = function(event) {
            var offsetX = event.offsetX || event.pageX;
            var offsetY = event.offsetY || event.pageY;
            if (offsetX !== undefined &&
                    offsetY !== undefined &&
                    offsetX > canvas.width - 30 - IMAGE.VOLUME_ON.width &&
                    offsetY < IMAGE.VOLUME_ON.height + 10) {
              // toggle sound
              if (soundOn = !soundOn) {
                AUDIO.MUSIC.volume = 0.5;
                AUDIO.JUMP.volume = 1;
                AUDIO.DEATH.volume = 1;
                AUDIO.WIN.volume = 1;
              } else {
                AUDIO.MUSIC.volume = 0;
                AUDIO.JUMP.volume = 0;
                AUDIO.DEATH.volume = 0;
                AUDIO.WIN.volume = 0;
              }
            }
          }
        }

        function waitForResources() {
          if (RBR.isImagesLoading()) {
            setTimeout(waitForResources, 250);
            return;
          }
          if (skipSplash) {
            startGame();
          } else {
            renderSplash();
          }
        }

        waitForResources();
      }
          
      if (canvas.getContext) {

        // if we're in an iframe and DON'T have
        // the standalone flag, assume we're being
        // displayed in Bitbucket as a Connect
        // File View
        if (RBR.inIframe() && !RBR.queryParam('standalone')) {
      
          // determine the context file from the
          // context parameters in the query
          var repo = RBR.queryParam('repo');
          var commit = RBR.queryParam('cset');
          var path = RBR.queryParam('path');

          // relative URL to the raw file end-point
          var rawUrl = '/1.0/repositories/{}/' + repo +
                      '/raw/' + commit +
                      '/' + path;

          if (RBR.requiresAuthentication(repo)) {
            // if this repository requires auth, use the
            // nifty cross-frame JavaScript bridge

            AP.require('request', function(request) {              

              request({              
                url: rawUrl,            
                responseType: "text/plain",
                success: function (rawSrc) {                
                  reinitGame(rawSrc);
                },
                error: function(err) {
                  document.querySelector("#content").innerHTML =
                          "Failed to load source file from Bitbucket. (" +
                            JSON.stringify(err) +
                          ")";
                }
              });          

            });

          } else {
            // if this repository is whitelisted, use CORS
            // (this avoids the auth prompt)

            rawUrl = "https://api.bitbucket.org" + rawUrl;

            superagent
              .get(rawUrl)              
              .set('Accept', 'text/plain')
              .end(function(err, res){
                if (err) {
                  document.querySelector("#content").innerHTML =
                          "Failed to load source file from Bitbucket. (" +
                            JSON.stringify(err) +
                          ")";
                } else {
                  reinitGame(res.text);
                }
              });

          }

        } else {
            
          // if we're not being rendered as a Bitbucket
          // add-on, revert to quine mode for testing
          reinitGame(document.documentElement.innerHTML);

        }
                
      } else {
        // :(
        document.querySelector("#content").innerHTML =
          "Sorry, your browser does not seem to support the canvas API.";
      }      
    </script>
    <script>
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
              m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

      ga('create', 'UA-69159384-2', 'auto');
      ga('send', 'pageview');
    </script>
  </body>
</html>