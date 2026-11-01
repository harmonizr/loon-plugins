# Loon 插件镜像（LoonLab）

从 [loonlab.103516.xyz](https://loonlab.103516.xyz/Plugin/) 同步的 **136** 个插件模块，纯备份 + 便于自维护。

- 源站索引更新时间：**2026-11-01 11:39**
- 本次同步时间：**2026-11-01 15:56:31**
- 插件源码目录：`plugins/`（均为 Loon `.lpx` 格式，可直接用文本编辑器改）
- 结构化元数据：`manifest.json`（含 sha256、原地址、作者、标签）
- 源站原始索引：`plugins.json`（前台 89 个）、`plugins.all.json`（全部 136 个）

## 目录结构

```
.
├── plugins/            # 136 个 .lpx 插件源码
├── manifest.json       # 带 sha256 的完整清单
├── plugins.all.json    # 源站全量索引
├── plugins.json        # 源站默认(展示)索引
├── index.md            # 纯表格索引
└── sync.py             # 增量同步脚本（--force 全量 / --check 只检查）
```

## 怎么用

**自己在 Loon 里安装本仓库的插件**（推送到 GitHub 后）：

```
https://raw.githubusercontent.com/<你的用户名>/<仓库名>/main/plugins/<文件名>.lpx
```

**修改插件**：直接编辑 `plugins/xxx.lpx`，开头 `#!name / #!desc / #!icon / #!tag` 是元信息，其余是 `[Script]`、`[Rewrite]`、`[MITM]`、`[Plugin]` 等段落。

**重新同步**（需要 Python 3）：

```bash
python3 sync.py          # 增量：只下载源站有更新/新增的插件
python3 sync.py --force  # 全量重下
```

> 同步要点：源站 `loon.103516.xyz` 对普通浏览器/curl 会把请求 302 跳去 Telegram，只有带 **Loon 客户端 UA**（`Loon/3.x CFNetwork/...`）才直接返回 `.lpx` 原文。脚本里已处理。

## 全部插件

| 插件 | 标签 | 作者 | 字节 | 更新时间 | 说明 |
|---|---|---|---|---|---|
| [1.1.1.1 with WARP](plugins/1.1.1.1.lpx) | 功能增强 | VirgilClyne, I-am-R-E | `2286` | 2026-10-02 12:00 | WARP检测面板与节点提取，点击下方主页链接前往配置1.1.1.1的BoxJs配置。 |
| [123云盘](plugins/123Pan.lpx) | 去广告 / 功能增强 | 可莉🅥, ddgksf2013 | `1416` | 2026-10-02 12:00 | 过滤123云盘应用端及网页端广告，解除网页端流量1G下载限制（请单文件下载，不要文件夹或多文件下载）。 |
| [爱回收](plugins/AiHuiShou.lpx) | 去广告 | ddgksf2013 | `6818` | 2026-10-02 12:00 | 过滤爱回收广告 |
| [阿里云盘](plugins/Alipan.lpx) | 去广告 | RuCu6, 可莉🅥 | `2167` | 2026-10-02 12:00 | 过滤阿里云盘广告 |
| [高德地图](plugins/Amap.lpx) | 去广告 | RuCu6, kokoryh, ishowshu, 可莉🅥 | `14225` | 2026-10-20 15:00 | 过滤高德地图广告 |
| [DNS防污染](plugins/Anti-DNS-Leaks.lpx) | 功能增强 | sooyaaabo | `1764` | 2026-10-02 12:00 | 指定可靠DNS解析，防止被污染或劫持 |
| [AppleOS Monitor](plugins/AppleOSMonitor.lpx) | 功能增强 / 定时任务 | sooyaaabo | `2482` | 2026-10-02 12:00 | 定时监控Apple系统的版本更新。\n可自定义选择需要监控的设备系统。\n可输入多个OS版本，不填则默认所有OS版本，以逗号分隔。\n可选择版本类型，默认为all即所有版本。\n可填入Bark Group分组名称，默认为… |
| [AppRaven](plugins/AppRaven.lpx) | 解锁会员 | Yu9191 | `690` | 2026-10-02 12:00 | AppRaven解锁会员 |
| [AppStore Monitor](plugins/AppStoreMonitor.lpx) | 功能增强 / 定时任务 | sooyaaabo | `1865` | 2026-10-02 12:00 | 定时监控App Store内App的更新状态。\n可输入多个AppID，可自定义查询区域顺序（不填则为默认顺序），均以逗号分隔。\n可填入Bark Key使用Bark推送通知，若不填则默认使用Loon推送通知。\n可填入… |
| [阿基米德](plugins/ArchimedesFM.lpx) | 去广告 | mist-whisper | `2378` | 2026-10-02 12:00 | 过滤阿基米德广告 |
| [百度地图](plugins/BaiduMap.lpx) | 去广告 | ddgksf2013 | `1993` | 2026-10-02 12:00 | 过滤百度地图广告 |
| [百度网盘](plugins/BaiduNetDisk.lpx) | 去广告 / 解锁会员 | 可莉🅥, ddgksf2013, chxm1023 | `4248` | 2026-10-02 12:00 | 过滤百度网盘广告，解锁部分SVIP功能。 |
| [百度贴吧](plugins/BaiduTieba.lpx) | 去广告 | app2smile, 可莉🅥 | `5449` | 2026-10-02 12:00 | 过滤百度贴吧广告 |
| [百度文库](plugins/BaiduWenku.lpx) | 去广告 | 可莉🅥 | `2105` | 2026-10-02 12:00 | 过滤百度文库广告 |
| [银行App](plugins/Bank.lpx) | 去广告 | 可莉🅥, fmz200 | `11033` | 2026-10-02 12:00 | 过滤部分银行应用广告 |
| [哔哩哔哩](plugins/Bilibili.lpx) | 去广告 | RuCu6, kokoryh, 可莉🅥 | `9172` | 2026-10-30 23:00 | 过滤哔哩哔哩广告 |
| [哔哩哔哩VIP](plugins/Bilibili_VIP.lpx) | 去广告 | ddgksf2013 | `1044` | 2026-10-05 00:00 | 哔哩哔哩大会员 |
| [广告拦截合集](plugins/BlockAds.lpx) | 去广告 | fmz200, zirawell | `170164` | 2026-10-31 00:00 | 针对部分APP和小程序广告进行拦截，某些APP要清除缓存或者重新安装拦截广告才会生效！ |
| [波点音乐](plugins/BodianMusic.lpx) | 去广告 / 解锁会员 | 可莉🅥, ZenmoFeiShi, mist-whisper, GieGie777 | `6594` | 2026-10-02 12:00 | 过滤波点音乐广告，解锁会员功能。\n使用前请在BoxJS中添加订阅https://raw.githubusercontent.com/Yuheng0101/X/main/Tasks/boxjs.json并同意相关免责声明… |
| [BoxJs](plugins/BoxJs.lpx) | 功能增强 | chavyleung | `872` | 2026-10-02 12:00 | Data manager，使用前请在本插件的详情页面为[PROXY]项分配代理策略。 |
| [菜鸟](plugins/CaiNiao.lpx) | 去广告 | githubdulong | `2270` | 2026-10-02 12:00 | 过滤菜鸟广告 |
| [财新](plugins/CaiXin.lpx) | 去广告 | ZenmoFeiShi | `1825` | 2026-10-02 12:00 | 过滤财新广告 |
| [超格教育](plugins/ChaoGeJiaoYu.lpx) | 去广告 | sooyaaabo | `1888` | 2026-10-05 15:00 | 过滤超格教育广告 |
| [车来了](plugins/CheLaiLe.lpx) | 去广告 | CaoXiaoMann | `1749` | 2026-10-14 11:00 | 过滤车来了广告 |
| [中国广电](plugins/ChinaBroadnet.lpx) | 去广告 | ddgksf2013 | `1188` | 2026-10-02 12:00 | 过滤中国广电广告 |
| [中国移动](plugins/ChinaMobile.lpx) | 去广告 / 功能增强 | ccyykk666, sooyaaabo, MaYIHEI | `8510` | 2026-10-27 17:00 | 过滤中国移动广告，可自定义。\n支持Scripting中国移动小组件（https://www.imarkr.com/api/github/download/MaYIHEI/patch/scripting/cmcc.zip… |
| [中国联通](plugins/ChinaUnicom.lpx) | 去广告 | mist-whisper | `2398` | 2026-10-02 12:00 | 过滤中国联通广告 |
| [CMS Adblocker](plugins/CMS_Adblock.lpx) | 去广告 | Yswag | `5429` | 2026-10-02 12:00 | 过滤CMS资源插入式广告 |
| [彩云天气Pro](plugins/ColorfulCloudsWeatherPro.lpx) | 去广告 / 解锁会员 | RuCu6, 可莉🅥 | `2134` | 2026-10-02 12:00 | 过滤彩云天气广告，解锁SVIP功能。\nApp版本低于7.20.2。 |
| [Cookie & Task](plugins/CookieTask.lpx) | 定时任务 | FoKit, GoodHolidays, ClydeTime, MaYIHEI, sooyaaabo | `6220` | 2026-10-02 12:00 | 定时每日签到任务，按需开启相应功能即可。 |
| [酷安](plugins/CoolApk.lpx) | 去广告 | RuCu6, ZenmoFeiShi, VenenoSix24, 可莉🅥 | `3764` | 2026-10-02 12:00 | 过滤酷安广告 |
| [小宇宙](plugins/CosmosFM.lpx) | 去广告 | mist-whisper | `1958` | 2026-10-02 12:00 | 过滤小宇宙广告 |
| [大麦](plugins/DaMai.lpx) | 去广告 | 可莉🅥 | `1451` | 2026-10-02 12:00 | 过滤大麦广告 |
| [得物](plugins/DeWu.lpx) | 去广告 | 可莉🅥 | `2471` | 2026-10-02 12:00 | 过滤得物广告 |
| [滴滴](plugins/DiDi.lpx) | 去广告 | sooyaaabo, ishowshu, ZenmoFeiShi, 可莉🅥 | `18181` | 2026-10-02 12:00 | 过滤滴滴广告 |
| [叮咚买菜](plugins/DingDongMaiCai.lpx) | 去广告 | mist-whisper, zirawell, 可莉🅥 | `4936` | 2026-10-02 12:00 | 过滤叮咚买菜广告 |
| [豆瓣](plugins/DouBan.lpx) | 去广告 | ishowshu, fmz200 | `967` | 2026-10-02 12:00 | 过滤豆瓣广告，仅去除开屏广告 |
| [香港抖音](plugins/Douyin_HK.lpx) | 去广告 | 可莉🅥 | `3259` | 2026-10-02 12:00 | 过滤香港抖音广告 |
| [萤石云视频](plugins/Ezviz.lpx) | 去广告 | 可莉🅥 | `1532` | 2026-10-02 12:00 | 过滤萤石云视频广告 |
| [帆书](plugins/FanShu.lpx) | 去广告 | Yuheng0101 | `4074` | 2026-10-02 12:00 | 过滤帆书（樊登读书）广告 |
| [粉笔](plugins/FenBi.lpx) | 去广告 | 可莉🅥, sooyaaabo | `3306` | 2026-10-02 12:00 | 过滤粉笔广告 |
| [Forward](plugins/Forward.lpx) | 解锁会员 | Yu9191 | `796` | 2026-10-02 12:00 | 解锁Forward Pro，适用于1.3.13及以下版本。 |
| [盒马](plugins/Freshippo.lpx) | 去广告 | 可莉🅥 | `3220` | 2026-10-02 12:00 | 过滤盒马广告 |
| [GitHub](plugins/GitHub.lpx) | 功能增强 | Yuheng0101, sooyaaabo | `1251` | 2026-10-02 12:00 | 解决GitHub 429请求频繁问题 |
| [GLaDOS](plugins/GLaDOS.lpx) | 定时任务 | curtinp118 | `1648` | 2026-10-02 12:00 | GLaDOS每日签到。访问网页登录账号，进入账户页面后，手动刷新一次网页自动获取保存Cookie。Cookie存在有效期，失效后需重新获取。 |
| [闲鱼](plugins/Goofish.lpx) | 去广告 | RuCu6, ZenmoFeiShi, ishowshu, 可莉🅥 | `10454` | 2026-10-20 12:00 | 过滤闲鱼广告 |
| [Google](plugins/Google.lpx) | 功能增强 | sooyaaabo | `937` | 2026-10-02 12:00 | 将Google搜索重定向至.com域名，如遇频繁跳转请禁用本插件。 |
| [喜马拉雅](plugins/HimalayaFM.lpx) | 去广告 | 可莉🅥 | `5198` | 2026-10-02 12:00 | 过滤喜马拉雅广告 |
| [王者营地](plugins/HOK_GameHelper.lpx) | 去广告 | 可莉🅥 | `1006` | 2026-10-02 12:00 | 过滤王者营地广告 |
| [虎扑](plugins/HUPU.lpx) | 去广告 | ishowshu | `3362` | 2026-10-29 19:00 | 过滤虎扑广告 |
| [IPA Manager](plugins/IPAManager.lpx) | 功能增强 | githubdulong | `990` | 2026-10-02 12:00 | 下载IPA文件实现降级应用安装、已购下架应用安装。\n本插件依赖Scripting App且需解锁Pro权限。 |
| [IPPure](plugins/IPPure.lpx) | 功能增强 | sooyaaabo | `511` | 2026-10-02 12:00 | 通过IPPure接口检测IP质量。 |
| [爱奇艺](plugins/IQIYI.lpx) | 去广告 | RuCu6, 可莉🅥 | `10224` | 2026-10-02 12:00 | 悦享品质 [悦享广告] |
| [爱奇艺体育](plugins/IQIYI_Ssports.lpx) | 去广告 | mist-whisper | `1162` | 2026-10-02 12:00 | 过滤爱奇艺体育广告 |
| [iRingo:WeatherKit](plugins/iRingo_WeatherKit.lpx) | 功能增强 | VirgilClyne, WordlessEcho, 001ProMax | `6074` | 2026-10-02 12:00 | 1.解锁全部天气功能；2.替换空气质量数据；3.添加下一小时降水数据；4.添加天气数据。\n仅支持iOS 18 & macOS 15 & watchOS 11及以上版本。 |
| [IT之家](plugins/IThome.lpx) | 去广告 | 可莉🅥 | `1285` | 2026-10-02 12:00 | 过滤IT之家广告，自定义移除置顶和轮播图，自定义移除项需在插件配置。 |
| [iTunes](plugins/iTunes.lpx) | 解锁会员 | chxm1023, ddgksf2013, Guding88 | `1933` | 2026-10-02 12:00 | iTunes系列解锁合集，在设置中选择需要使用的原作者脚本以使用此插件。 |
| [iTunes](plugins/iTunes_baby.lpx) | 解锁会员 | ios151 | `1398` | 2026-10-06 17:00 | 自动查询App内购产品，并解锁最高价套餐的订阅凭证；可在插件设置中关闭。 |
| [京东](plugins/JingDong.lpx) | 去广告 / 功能增强 | RuCu6, Maasea, MuTu, 苍井灰灰, mw418, 可莉🅥 | `5424` | 2026-10-02 12:00 | 1.过滤京东广告；2.历史比价信息，任选其一即可。（首次使用请先打开【慢慢买App-我的】，提示【获取ck成功🎉】即可正常比价。）\n此插件仅支持京东标准模式。 |
| [京东外卖](plugins/JingdongWaimai.lpx) | 去广告 | 可莉🅥 | `2105` | 2026-10-02 12:00 | 过滤京东外卖广告 |
| [金山文档](plugins/KDocs.lpx) | 去广告 | 可莉🅥 | `1059` | 2026-10-02 12:00 | 过滤金山文档广告 |
| [Keep](plugins/Keep.lpx) | 去广告 | 可莉🅥, ZenmoFeiShi, ishowshu | `5458` | 2026-10-02 12:00 | 过滤Keep广告 |
| [酷我音乐](plugins/KuwoMusic.lpx) | 去广告 / 解锁会员 | 可莉🅥, Yuheng0101 | `5338` | 2026-10-02 12:00 | 过滤酷我音乐广告，解锁会员功能。\n使用前请在BoxJS中添加订阅https://raw.githubusercontent.com/Yuheng0101/X/main/Tasks/boxjs.json并同意相关免责声明… |
| [快手](plugins/Kwai.lpx) | 去广告 | 可莉🅥 | `3101` | 2026-10-02 12:00 | 过滤快手广告 |
| [Listenify](plugins/Listenify.lpx) | 功能增强 | Yswag | `721` | 2026-10-02 12:00 | 从网易云音乐获取歌词与艺人封面 |
| [掌上英雄联盟](plugins/LOL_Bible.lpx) | 去广告 | 可莉🅥 | `1695` | 2026-10-02 12:00 | 过滤掌上英雄联盟广告 |
| [Loon Gallery](plugins/LoonGallery.lpx) | 功能增强 | Peng-YM | `837` | 2026-10-02 12:00 | Loon插件仓库，一键安装。使用前请在本插件的详情页面为[PROXY]项分配代理策略。 |
| [本机开发服务回环](plugins/Loopback.lpx) | 开发工具 | sooyaaabo | `940` | 2026-10-10 20:00 | 将发往目标IP的流量导入TUN并重定向回本机，用于本地开发调试。目标服务需已在本机监听。 |
| [瑞幸咖啡](plugins/LuckinCoffee.lpx) | 去广告 | Sliverkiss, 可莉🅥 | `1634` | 2026-10-02 12:00 | 过滤瑞幸咖啡广告 |
| [马蜂窝](plugins/MaFengWo.lpx) | 去广告 | 可莉🅥 | `1103` | 2026-10-02 12:00 | 过滤马蜂窝广告 |
| [埋堆堆](plugins/MaiDuiDui.lpx) | 去广告 | ddgksf2013 | `1776` | 2026-10-02 12:00 | 过滤埋堆堆广告 |
| [芒果TV](plugins/MangoTV.lpx) | 去广告 / 解锁会员 | RuCu6, WeiGiegie, 可莉🅥 | `5773` | 2026-10-02 12:00 | 天生青春 [天生广告] |
| [美柚](plugins/MeetYou.lpx) | 去广告 | ddgksf2013, 可莉🅥 | `1672` | 2026-10-02 12:00 | 过滤美柚广告 |
| [美团](plugins/MeiTuan.lpx) | 去广告 | ZenmoFeiShi | `5176` | 2026-10-25 21:00 | 过滤美团广告，需卸载重装。 |
| [咪咕视频](plugins/MiguVideo.lpx) | 去广告 / 解锁会员 | ddgksf2013 | `2172` | 2026-10-02 12:00 | 过滤咪咕视频广告 |
| [米游社](plugins/miHoYoBBS.lpx) | 去广告 | 可莉🅥 | `1802` | 2026-10-02 12:00 | 过滤米游社广告 |
| [MyBlockAds](plugins/MyBlockAds.lpx) | 去广告 | RuCu6 | `26451` | 2026-10-08 10:00 | Walalala自用去广告合集 |
| [网易云音乐](plugins/NeteaseMusic.lpx) | 去广告 / 解锁会员 | RuCu6, Keywos, 可莉🅥 | `10059` | 2026-10-16 22:00 | 网易云音乐全面净化，可自定义界面样式。 |
| [网络信息 𝕏](plugins/Netisp-x.lpx) | 功能增强 | Keywos, xream | `1640` | 2026-10-02 12:00 | 长按节点进行网络信息查询；支持网络变化时进行查询通知；提供 https://net-lsp-x.com 数据接口；详细参数设置见频道说明：https://t.me/zhetengsha |
| [NodeSeek & DeepFlood](plugins/NodeSeek.lpx) | 定时任务 | sooyaaabo | `2521` | 2026-10-02 12:00 | NodeSeek、DeepFlood每日签到。\n登录账号进入个人页面以获取Cookie，成功后关闭Cookie脚本。\n支持设置签到鸡腿奖励模式，默认为固定5个鸡腿。 |
| [节点检测工具 𝕂](plugins/NodeTools.lpx) | 功能增强 | KOP-XIAO, xream, Keywos, dcpengx, 可莉🅥 | `1656` | 2026-10-02 12:00 | 节点网速测试、节点解锁状况、节点风险查询、节点入口落地查询 |
| [PandaTV](plugins/PandaTV.lpx) | 功能增强 | sooyaaabo | `799` | 2026-10-02 12:00 | 绕过PandaTV直播源防盗检测，恢复正常播放。 |
| [拼多多](plugins/PinDuoDuo.lpx) | 去广告 | sooyaaabo, ZenmoFeiShi, RuCu6, ishowshu, 可莉🅥 | `8390` | 2026-10-02 12:00 | 过滤拼多多广告 |
| [QQ](plugins/QQ.lpx) | 功能增强 | 可莉🅥 | `2021` | 2026-10-02 12:00 | QQ链接解锁，解除QQ内访问非白名单之外的地址提示停止访问该页面的限制，并移除跟踪参数。使用前需要清除QQ的缓存数据。 |
| [QQ音乐](plugins/QQMusic.lpx) | 去广告 | 可莉🅥 | `918` | 2026-10-02 12:00 | 过滤QQ音乐广告 |
| [夸克](plugins/QuarkBrowser.lpx) | 去广告 | 可莉🅥 | `28779` | 2026-10-02 12:00 | 过滤夸克广告 |
| [夸克扫描王](plugins/QuarkScanKing.lpx) | 去广告 | 可莉🅥 | `6094` | 2026-10-02 12:00 | 过滤夸克扫描王广告 |
| [和风天气](plugins/QWeather.lpx) | 去广告 | ddgksf2013 | `652` | 2026-10-02 12:00 | 过滤和风天气广告 |
| [铁路12306](plugins/Railway12306.lpx) | 去广告 | RuCu6, kokoryh | `1073` | 2026-10-02 12:00 | 过滤铁路12306广告 |
| [Reddit](plugins/Reddit.lpx) | 去广告 | xream, 可莉🅥 | `774` | 2026-10-02 12:00 | 过滤应用内推广，阻止NSFW提示。 |
| [Redirect](plugins/Redirect.lpx) | 功能增强 | blackmatrix7 | `9973` | 2026-10-02 12:00 | 针对部分网站进行重定向 |
| [小红书](plugins/RedNote.lpx) | 去广告 | RuCu6, fmz200, meichiny, 可莉🅥 | `7279` | 2026-10-02 12:00 | 过滤小红书广告，去除水印 |
| [RevenueCat](plugins/RevenueCat.lpx) | 解锁会员 | chxm1023, ddgksf2013, Guding88 | `3085` | 2026-10-02 12:00 | RevenueCat系列解锁合集，在设置中选择需要使用的原作者脚本以使用此插件。 |
| [RevenueCat](plugins/RevenueCat_baby.lpx) | 解锁会员 | ios151 | `1656` | 2026-10-06 17:00 | 支持解锁RevenueCat、Superwall和Adapty（Adapty需卸载重装后生效）。\n遇到解锁后报错或闪退的 App，可在插件设置中填入名称跳过；默认「-」表示全部 App 解锁。 |
| [Script Hub](plugins/Script-Hub.lpx) | 功能增强 | xream, Keywos, CKYB, 小白脸 | `2266` | 2026-10-02 21:00 | 重写 & 规则集转换，使用前请在本插件的详情页面为[PROXY]项分配代理策略。 |
| [顺丰速运](plugins/SF-Express.lpx) | 去广告 | 可莉🅥 | `27575` | 2026-10-02 12:00 | 过滤顺丰速运广告 |
| [Skip Proxy and Real-IP Lists](plugins/SkipProxy.lpx) | 功能增强 | mieqq | `1554` | 2026-10-02 12:00 | 跳过部分应用的代理检测 |
| [什么值得买](plugins/smzdm.lpx) | 去广告 | ZenmoFeiShi, 可莉🅥 | `8713` | 2026-10-02 12:00 | 过滤什么值得买广告 |
| [汽水音乐](plugins/SodaMusic.lpx) | 去广告 | 可莉🅥 | `4327` | 2026-10-02 12:00 | 过滤汽水音乐广告 |
| [Soul](plugins/Soul.lpx) | 去广告 | ZenmoFeiShi, ishowshu, RuCu6, 可莉🅥 | `10778` | 2026-10-02 12:00 | Soul全面净化 |
| [SourceCode](plugins/SourceCode.lpx) | 功能增强 | sooyaaabo | `8083` | 2026-10-02 12:00 | 支持浏览器内查看非公开插件源码，支持将插件转换为其他代理客户端所支持的格式。 |
| [Spotify](plugins/Spotify.lpx) | 去广告 | 001ProMax, 可莉🅥 | `1819` | 2026-10-02 12:00 | 过滤Spotify广告，修改插件自定义配置项需要重新登陆方可生效。适用于9.1.14及以下版本。 |
| [Spotify](plugins/Spotify_CN.lpx) | 去广告 / 会员解锁 | devchristian1337 | `4245` | 2026-10-20 19:00 | 移除Spotify广告并解锁部分高级功能。音质无法设置为“极高（Very High）”。设置中Protobuf脚本只能启用其中一个，不能同时启用。启用插件后，请重新登录以应用完整配置。 |
| [墨鱼去开屏2.0](plugins/StartUpAds.lpx) | 去广告 | ddgksf2013 | `79036` | 2026-10-22 12:00 | 去除开屏广告，部分APP要清除缓存或者重新安装拦截广告才会生效! |
| [流媒体解锁测试](plugins/StreamingMedia.lpx) | 功能增强 | huskydsb | `6646` | 2026-10-02 12:00 | 设置不同流媒体规则所经策略组，访问服务检测网页（https://streaming.test），点击所需要测试的流媒体卡片，等待测试结果即可。 |
| [Sub-Store](plugins/Sub-Store.lpx) | 功能增强 | Peng-YM | `1955` | 2026-10-02 12:00 | 高级订阅管理工具。使用前请在本插件的详情页面为[PROXY]项分配代理策略。定时任务默认为每天23点55分，可在插件设置中自定义。定时任务指定时将订阅/文件上传到私有Gist。在前端，叫做'同步'或'同步配置'。 |
| [淘宝](plugins/TaoBao.lpx) | 去广告 | RuCu6, ishowshu, 可莉🅥 | `3763` | 2026-10-02 12:00 | 过滤淘宝广告 |
| [飞猪旅行](plugins/TaobaoTravel.lpx) | 去广告 | 可莉🅥 | `1351` | 2026-10-02 12:00 | 过滤飞猪旅行广告 |
| [淘票票](plugins/TaoPiaoPiao.lpx) | 去广告 | 可莉🅥 | `2019` | 2026-10-02 12:00 | 过滤淘票票广告 |
| [Telegram](plugins/Telegram.lpx) | 功能增强 | sooyaaabo | `2479` | 2026-10-02 12:00 | Telegram外部链接跳转，可选目标客户端为Telegram、Swiftgram、Nagram、Turrit、iMe、Nicegram、Lingogram，默认选择Telegram跳转至官方客户端。 |
| [腾讯文档](plugins/TencentDocs.lpx) | 去广告 | 可莉🅥 | `830` | 2026-10-02 12:00 | 过滤腾讯文档广告 |
| [腾讯视频](plugins/TencentVideo.lpx) | 去广告 | ZenmoFeiShi | `3138` | 2026-10-27 16:00 | 不负好时光 [不负好广告] |
| [TestFlight](plugins/TestFlight.lpx) | 功能增强 | NobyDa, 可莉🅥 | `1323` | 2026-10-02 12:00 | 解除TestFlight区域限制，以解决安装或更新TestFlight内App时, 提示“APP不可用”问题。\niOS/iPadOS/tvOS 26已禁止TestFlight MitM，请禁用此插件。 |
| [TestFlight Monitor](plugins/TestFlightMonitor.lpx) | 功能增强 / 定时任务 | fmz200, DecoAri, xream | `1980` | 2026-10-02 12:00 | 1.自动监控TestFlight，手动填写应用APP_ID，一旦有空余名额会自动通知，点击通知即可跳转加入；\n2.自动加入TestFlight，需先获取账号令牌[添加主机名testflight.apple.com]，一… |
| [迅雷](plugins/ThunderCloudDisk.lpx) | 去广告 / 解锁会员 | 可莉🅥, Marol62926 | `1690` | 2026-10-02 12:00 | 过滤迅雷广告，解锁部分会员功能。 |
| [UAPI热榜聚合](plugins/UAPI_HotBoard.lpx) | 定时任务 | sooyaaabo | `2188` | 2026-10-02 12:00 | 基于UAPI热榜接口定时推送多平台热榜数据。\n可选填UAPI Token，使用个人密钥将消耗积分。\n可设置热榜平台，建议避免配置过多以减少请求频率。\n可设置榜单条数，默认5条，最大10条。\n支持平台：哔哩哔哩 b… |
| [航旅纵横](plugins/Umetrip.lpx) | 去广告 | ddgksf2013 | `1643` | 2026-10-05 15:00 | 过滤航旅纵横广告 |
| [V2EX](plugins/V2EX.lpx) | 去广告 | ddgksf2013, curtinp118 | `1955` | 2026-10-02 12:00 | 过滤V2EX社区广告；V2EX每日签到，访问V2EX个人主页自动获取保存Cookie。 |
| [看理想](plugins/Vistopia.lpx) | 去广告 / 解锁会员 | ios151, Aioneas | `3457` | 2026-10-27 23:00 | 过滤看理想部分广告，解锁会员广告及无限畅听，暂不支持数字图书馆。\n视频解析：进入视频课程详情页，点击右上角分享并复制链接，在浏览器中打开，进入播放面板后点击任意一集即可自动解析。 |
| [VVebo](plugins/VVebo.lpx) | 功能增强 | suiyuran, androidcn | `1547` | 2026-10-02 12:00 | 修复用户主页时间线问题，需禁用[微博]插件和[微博轻享版]插件，以避免本插件不生效。 |
| [WebPage](plugins/WebPage.lpx) | 去广告 | RuCu6, kokoryh | `7151` | 2026-10-31 22:00 | 过滤部分网页广告 |
| [微信](plugins/WeChat.lpx) | 去广告 | RuCu6, zZPiglet, blackmatrix7, zirawell, 可莉🅥 | `37594` | 2026-10-02 12:00 | 微信公众号、小程序去广告以及微信外部链接解锁 |
| [微博](plugins/WeiBo.lpx) | 去广告 | RuCu6, fmz200, zmqcherish, 可莉🅥 | `10592` | 2026-10-19 15:00 | 微博全面净化 |
| [微博](plugins/WeiBo_ddgksf2013.lpx) | 去广告 | ddgksf2013 | `2344` | 2026-10-19 20:00 | 微博增强 |
| [微博轻享版](plugins/WeiBo_Intl.lpx) | 去广告 | Keywos, kokoryh, 可莉🅥 | `3745` | 2026-10-02 12:00 | 过滤微博轻享版广告 |
| [微店](plugins/WeiDian.lpx) | 去广告 | 可莉🅥 | `2455` | 2026-10-02 12:00 | 过滤微店广告 |
| [X（Twitter）](plugins/X_Web.lpx) | 去广告 | fmz200, sooyaaabo | `2210` | 2026-10-02 12:00 | 过滤网页版X（Twitter）广告，支持自定义标签。\n所有标签：政治, 股票, 商业, 科学, AI, 加密, 新闻, 金融, 软件, 体育, 科技, 艺术, 电影与电视, 游戏, 橄榄球, 动漫, 旅行, 美食, 棒… |
| [小蚕惠生活](plugins/XiaoCan.lpx) | 去广告 | Sliverkiss, 可莉🅥 | `1521` | 2026-10-02 12:00 | 过滤小蚕惠生活广告 |
| [小黑盒](plugins/XiaoHeiHe.lpx) | 去广告 | 可莉🅥 | `1007` | 2026-10-02 12:00 | 过滤小黑盒广告 |
| [小象超市](plugins/XiaoxiangSupermarket.lpx) | 去广告 | 可莉🅥 | `1712` | 2026-10-02 12:00 | 过滤小象超市广告 |
| [XPTV](plugins/XPTV.lpx) | 功能增强 | Yswag | `3706` | 2026-10-02 12:00 | 伪CMS源，安装此插件后在XPTV内添加订阅地址：https://ykusu.ykusu/getJSON/cmsbeta.json |
| [雪球](plugins/XueQiu.lpx) | 去广告 | 可莉🅥, ddgksf2013 | `4297` | 2026-10-02 12:00 | 过滤雪球广告 |
| [优酷视频](plugins/YoukuVideo.lpx) | 去广告 | RuCu6, 可莉🅥 | `3793` | 2026-10-02 12:00 | 为好内容 全力以赴 [为好广告 全力以赴] |
| [YouTube (Music)](plugins/YouTube.lpx) | 去广告 / 功能增强 | Maasea, RuCu6 | `2810` | 2026-10-02 12:00 | 过滤YouTube (Music)广告，增加画中画、字幕翻译、歌词翻译功能，支持后台播放。需要启用QUIC回退保护。不支持tvOS设备。 |
| [YouTube](plugins/YouTube_CN.lpx) | 去广告 / 功能增强 | devchristian1337 | `10700` | 2026-10-10 16:00 | 移除YouTube应用广告、启用后台播放，并翻译现有字幕轨道（目标语言为zh-CN或en-US；没有字幕的视频无法翻译）。默认仅记录媒体响应头；完整采样可能增加延迟。\n该插件基于devchristian1337的You… |
| [知乎](plugins/ZhiHu.lpx) | 去广告 | RuCu6, blackmatrix7, 可莉🅥 | `12530` | 2026-10-02 12:00 | 过滤知乎广告 |

## 说明

- 本仓库仅为个人备份与学习维护之用，所有插件版权归各自原作者；上游站声明「禁止在境内平台公开传播、禁止用于商业或非法用途」，请自行遵守。
- 插件内引用的远端脚本（raw.githubusercontent.com 等）仍由原作者维护，此处只镜像 `.lpx` 本体。
