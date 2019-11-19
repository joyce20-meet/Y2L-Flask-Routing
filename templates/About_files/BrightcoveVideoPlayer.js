$(document).ready(function () {

    // Select all a-tags with attribute "data-playerid"
    $("[data-playerid]").on("click",
        function (e) {
            BrightcoveVideoPlayer.showMovieFromDirectLink(this);
            e.preventDefault();
            return false;
        });

});

var BrightcoveVideoPlayerClass = function () {
    var drawBrightcoveObject = function (video) {
        var playerData = {
            "accountId": "1464976755001",
            "playerId": video.PlayerId,
            "videoId": video.VideoId
        };
        const playerHtml = "<video id=\"myPlayerID\" data-video-id=\"" + playerData.videoId + '\"  data-account=\"' + playerData.accountId + '\" data-player=\"' + playerData.playerId + '\" data-embed=\"default\" class=\"video-js\" controls></video>';
        // Inject the player code into the DOM
        document.getElementById("videoloader").innerHTML = playerHtml;
        // Add and execute the player script tag
        const bcscript = document.createElement("script");
        bcscript.src = "//players.brightcove.net/" + playerData.accountId + "/" + playerData.playerId + "_default/index.min.js";
        // Add the script tag to the document
        document.body.appendChild(bcscript);

    };
    var loadMovieDialog = function (container, video) {

        // Create container
        container.append("<div class=\"overlayPlayerBackground\"/>");

        const overlayVideo = $("<div class=\"overlayPlayer\"/>");
        const overlayClose = $("<div class=\"overlayPlayerClose\"/>");
        const overlayCloseLink = $("<a href=\"\"></a>");

        // Configure the closebutton, to unload dialog and brightcove player
        $(".overlayPlayerClose a").on("click", function (e) { 
            e.preventDefault();
            $(".overlayPlayer").remove();
            $(".overlayPlayerBackground").remove();
            return false;
        });
        const overlayVideoContainer = $("<div id='videoloader'/>");

        overlayCloseLink.appendTo(overlayClose);
        overlayClose.appendTo(overlayVideo);
        overlayVideoContainer.appendTo(overlayVideo);
        container.append(overlayVideo);
        // Create the player
        const playerOutput = drawBrightcoveObject(video);
        $(playerOutput).appendTo(overlayVideo);
        overlayVideo.fadeIn();

    };

    // private VideoClass
    var VideoClass = function () {
        var playerId;
        var playerKey;
        var videoId;
        var playerWidth;
        var playerHeight;
        var playerBackgroundColor;
        var playerAutostart;

        this.PlayerId = function (val) {
            if (val) {
                playerId = val;
            }
            return playerId;
        };

        this.PlayerKey = function (val) {
            if (val) {
                playerKey = val;
            }
            return playerKey;
        };

        this.VideoId = function (val) {
            if (val) {
                videoId = val;
            }
            return videoId;
        };

        this.PlayerWidth = function (val) {
            if (val) {
                playerWidth = val;
            }
            return playerWidth;
        };

        this.PlayerHeight = function (val) {
            if (val) {
                playerHeight = val;
            }
            return playerHeight;
        };

        this.PlayerBackgroundColor = function (val) {
            if (val) {
                playerBackgroundColor = val;
            }
            return playerBackgroundColor;
        };

        this.PlayerAutostart = function (val) {
            if (val) {
                playerAutostart = val;
            }
            return playerAutostart;
        };

    };
    var createVideoObject = function (element) {
        var link = $(element);
        var video = new VideoClass();
        video.PlayerId = link.attr("data-playerid");
        video.PlayerKey = link.attr("data-playerkey");
        video.VideoId = link.attr("data-videoid");
        video.PlayerWidth = link.attr("data-videowidth");
        video.PlayerHeight = link.attr("data-videoheight");
        video.PlayerBackgroundColor = link.attr("data-backgroundcolor");
        video.PlayerAutostart = link.attr("data-autostart");
        return video;
    };
    this.showMovieFromDirectLink = function (element) {

        const container = $(".main");
        var link = $(element);
        loadMovieDialog(container, createVideoObject(link));
        return false;
    };

};

// Create the global object
var BrightcoveVideoPlayer = new BrightcoveVideoPlayerClass();