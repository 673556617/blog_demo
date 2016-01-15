$(function() {


    // 播放器
    var Player = {
        // 歌曲路径
        path : 'http://zard-music.gz.bcebos.com/mp3/',
        //path:"/new_blog/zard/music/",

        // 歌曲数据
        data : null,

        // names
        captions :null,

        // 当前播放歌曲的 索引
        currentIndex : -1,

        //  播放器元素jquery对象
        $audio : $('audio'),

        // 歌曲列表
        $mList : $('#m-list'),

        //正在播放的歌曲
        $rmusic : $('#rmusic'),

        // 初始化 数据
        init : function() {

            // 数据一般来自服务器端,通过ajax 加载数据,这里是模拟
            Player.data = ["Zard%20-%20Can%27t%20Take%20My%20Eyes%20Off%20of%20You.mp3?authorization=bce-auth-v1%2F71a5f9df46cd4bce893693ac3b98c980%2F2016-01-10T04%3A12%3A40Z%2F599999940%2Fhost%2F9c11a572273fa53e2f84ef90323d4d554bb84b067dd47035bfbf0eb30f75a2a1",
                            "Zard%20-%20Get%20U%27re%20Dream.mp3?authorization=bce-auth-v1%2F71a5f9df46cd4bce893693ac3b98c980%2F2016-01-10T04%3A13%3A59Z%2F599999940%2Fhost%2F5662d3cdb18c8f3b3cc5588ec3aff9dbf372e60cb95132d5742745e3e19aa3d4",
                            "Zard%20-%20Seven%20Rainbow%20-%20ZARD%28%E3%81%A8%E3%81%8D%E3%82%81%E3%81%8D%E3%83%A1%E3%83%A2%E3%83%AA%E3%82%A2%E3%83%AB3%20%E3%82%AA%E3%83%BC%E3%83%95%E3%82%9A%E3%83%8B%E3%83%B3%E3%82%AF%E3%82%99%E3%83%86%E3%83%BC%E3%83%9E%29.mp3?authorization=bce-auth-v1%2F71a5f9df46cd4bce893693ac3b98c980%2F2016-01-10T04%3A15%3A06Z%2F59999940%2Fhost%2F757535542a7a06f28f96424c3dca982794d5501126915a15d7298616b1abfc02",
            ]
            Player.captions = ["Can't Take My Eyes Off of You",
                "Get U're Dream",
                "Seven Rainbow"];
            // 一般用模板引擎,把数据 与 模板 转换为 视图,来显示,这里是模拟
            var mhtml = '';
            var len = Player.data.length;
            for (var i = 0; i < len; i++) {
                currentSong = Player.data[i]
                mhtml += '<li><a index="' + i + '">' + Player.data[i] + '</a></li>';
                $('#musiclist').append('<li><a href="#" name =currentSong>'+Player.captions[i]+'</a></li>');

            }
            Player.$mList.html(mhtml);
             //alert("load playlist")

        },

        // 就绪
        ready : function() {

            // 控制

            Player.audio = Player.$audio.get(0);

            $('#ctrl-area').on('click', 'button', function() {
                Player.$rmusic.html(Player.data[Player.currentIndex]);
            });

            // 播放
            $('#btn-play').click(function() {
                //alert("click play")
                Player.audio.play();
                if (Player.currentIndex == -1) {
                    $('#btn-next').click();
                }
            });

            // 暂停
            $('#btn-stop').click(function() {
                //Player.audio.pause();
                Player.audio.pause();
            });

            // 下一曲
            $('#btn-next').click(function() {
                if (Player.currentIndex == -1) {
                    Player.currentIndex = 0;
                } else if (Player.currentIndex == (Player.data.length - 1)) {
                    Player.currentIndex = 0;
                } else {
                    Player.currentIndex++;
                }
                console.log("Player.currentIndex : " + Player.currentIndex);
                Player.audio.src = Player.path + Player.data[Player.currentIndex];
                Player.audio.play();
            });

            // 上一曲
            $('#btn-pre').click(function() {
                if (Player.currentIndex == -1) {
                    Player.currentIndex = 0;
                } else if (Player.currentIndex == 0) {
                    Player.currentIndex = (Player.data.length - 1);
                } else {
                    Player.currentIndex--;
                }
                Player.audio.src = Player.path + Player.data[Player.currentIndex];
                Player.audio.play();
            });

            // 单曲循环
            $('#btn-loop').click(function() {
                console.log("Player.currentIndex :", Player.currentIndex);
                Player.audio.onended = function() {
                    Player.audio.load();
                    Player.audio.play();
                };
            });

            // 顺序播放
            $('#btn-order').click(function() {
                console.log("Player.currentIndex :", Player.currentIndex);
                Player.audio.onended = function() {
                    $('#btn-next').click();
                };
            });

            // 随机播放
            $('#btn-random').click(function() {
                Player.audio.onended = function() {
                    var i = parseInt((Player.data.length - 1) * Math.random());
                    playByMe(i);
                };
            });

            // 播放指定歌曲
            function playByMe(i) {
                console.log("index:", i);
                Player.audio.src = Player.path + Player.data[i];
                Player.audio.play();
                Player.currentIndex = i;
                Player.$rmusic.html(Player.data[Player.currentIndex]);
            }

            // 歌曲被点击
            $('#m-list a').click(function() {
                playByMe($(this).attr('index'));
            });
        }
    };

    Player.init();
    Player.ready();

});
