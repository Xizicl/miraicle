(self.webpackChunkmiraicle_document=self.webpackChunkmiraicle_document||[]).push([[310],{3905:function(e,t,r){"use strict";r.d(t,{Zo:function(){return c},kt:function(){return d}});var n=r(7294);function i(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function o(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function a(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?o(Object(r),!0).forEach((function(t){i(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function l(e,t){if(null==e)return{};var r,n,i=function(e,t){if(null==e)return{};var r,n,i={},o=Object.keys(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||(i[r]=e[r]);return i}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(i[r]=e[r])}return i}var p=n.createContext({}),s=function(e){var t=n.useContext(p),r=t;return e&&(r="function"==typeof e?e(t):a(a({},t),e)),r},c=function(e){var t=s(e.components);return n.createElement(p.Provider,{value:t},e.children)},u={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},m=n.forwardRef((function(e,t){var r=e.components,i=e.mdxType,o=e.originalType,p=e.parentName,c=l(e,["components","mdxType","originalType","parentName"]),m=s(r),d=i,f=m["".concat(p,".").concat(d)]||m[d]||u[d]||o;return r?n.createElement(f,a(a({ref:t},c),{},{components:r})):n.createElement(f,a({ref:t},c))}));function d(e,t){var r=arguments,i=t&&t.mdxType;if("string"==typeof e||i){var o=r.length,a=new Array(o);a[0]=m;var l={};for(var p in t)hasOwnProperty.call(t,p)&&(l[p]=t[p]);l.originalType=e,l.mdxType="string"==typeof e?e:i,a[1]=l;for(var s=2;s<o;s++)a[s]=r[s];return n.createElement.apply(null,a)}return n.createElement.apply(null,r)}m.displayName="MDXCreateElement"},9353:function(e,t,r){"use strict";r.r(t),r.d(t,{frontMatter:function(){return l},contentTitle:function(){return p},metadata:function(){return s},toc:function(){return c},default:function(){return m}});var n=r(2122),i=r(9756),o=(r(7294),r(3905)),a=["components"],l={sidebar_position:3},p="\u5f00\u59cb\u4f7f\u7528",s={unversionedId:"guides/start-to-use",id:"guides/start-to-use",isDocsHomePage:!1,title:"\u5f00\u59cb\u4f7f\u7528",description:"\u9996\u5148\u542f\u52a8 mirai-console \u5e76\u767b\u9646\u4f60\u7684\u673a\u5668\u4eba\u8d26\u53f7\u3002\u4f60\u53ef\u4ee5\u67e5\u770b mirai-console \u7684\u6587\u6863\uff0c\u6216\u8005\u5728 mirai-console \u4e2d\u8f93\u5165 /help \u6765\u5b66\u4e60\u5982\u4f55\u4f7f\u7528\u3002",source:"@site/docs/guides/3-start-to-use.md",sourceDirName:"guides",slug:"/guides/start-to-use",permalink:"/miraicle/docs/guides/start-to-use",editUrl:"https://github.com/facebook/docusaurus/edit/master/website/docs/guides/3-start-to-use.md",version:"current",sidebarPosition:3,frontMatter:{sidebar_position:3},sidebar:"guides",previous:{title:"\u73af\u5883\u642d\u5efa",permalink:"/miraicle/docs/guides/install"},next:{title:"\u53d1\u751f\u4e86\u4ec0\u4e48\uff1f",permalink:"/miraicle/docs/guides/what-happened"}},c=[],u={toc:c};function m(e){var t=e.components,r=(0,i.Z)(e,a);return(0,o.kt)("wrapper",(0,n.Z)({},u,r,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"\u5f00\u59cb\u4f7f\u7528"},"\u5f00\u59cb\u4f7f\u7528"),(0,o.kt)("p",null,"\u9996\u5148\u542f\u52a8 ",(0,o.kt)("inlineCode",{parentName:"p"},"mirai-console")," \u5e76\u767b\u9646\u4f60\u7684\u673a\u5668\u4eba\u8d26\u53f7\u3002\u4f60\u53ef\u4ee5\u67e5\u770b ",(0,o.kt)("a",{parentName:"p",href:"https://github.com/mamoe/mirai-console"},(0,o.kt)("inlineCode",{parentName:"a"},"mirai-console"))," \u7684\u6587\u6863\uff0c\u6216\u8005\u5728 ",(0,o.kt)("inlineCode",{parentName:"p"},"mirai-console")," \u4e2d\u8f93\u5165 ",(0,o.kt)("inlineCode",{parentName:"p"},"/help")," \u6765\u5b66\u4e60\u5982\u4f55\u4f7f\u7528\u3002"),(0,o.kt)("p",null,"\u73b0\u5728\u4e00\u5207\u5de5\u4f5c\u5df2\u7ecf\u51c6\u5907\u5b8c\u6210\uff0c\u4f60\u53ef\u4ee5\u5f00\u59cb\u52a8\u624b\u5199\u81ea\u5df1\u7684 bot \u4e86\u3002\u6253\u5f00\u4f60\u6700\u719f\u6089\u7684\u7f16\u8f91\u5668\u6216 IDE \uff0c\u521b\u5efa\u4e00\u4e2a\u540d\u4e3a ",(0,o.kt)("inlineCode",{parentName:"p"},"bot.py")," \u7684\u6587\u4ef6\uff0c\u5185\u5bb9\u5982\u4e0b\uff1a"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-python",metastring:"title='bot.py'",title:"'bot.py'"},"import miraicle\n\n\n@miraicle.Mirai.receiver('GroupMessage')\ndef hello_to_group(bot: miraicle.Mirai, msg: miraicle.GroupMessage):\n    bot.send_group_msg(group=msg.group, msg='Hello world!')\n\n\n@miraicle.Mirai.receiver('FriendMessage')\ndef hello_to_friend(bot: miraicle.Mirai, msg: miraicle.FriendMessage):\n    bot.send_friend_msg(qq=msg.sender, msg='Hello world!')\n\n\nqq = 123456789              # \u4f60\u767b\u5f55\u7684\u673a\u5668\u4eba QQ \u53f7\nverify_key = 'miraicle'     # \u4f60\u5728 setting.yml \u4e2d\u8bbe\u7f6e\u7684 verifyKey\nport = 8080                 # \u4f60\u5728 setting.yml \u4e2d\u8bbe\u7f6e\u7684 port (http)\n\nbot = miraicle.Mirai(qq=qq, verify_key=verify_key, port=port)\nbot.run()\n")),(0,o.kt)("p",null,"\u5c06\u53d8\u91cf ",(0,o.kt)("inlineCode",{parentName:"p"},"qq")," \u4fee\u6539\u4e3a\u4f60\u767b\u5f55\u7684\u673a\u5668\u4eba\u7684 QQ \u53f7\uff0c\u5e76\u6839\u636e\u4f60\u5728 ",(0,o.kt)("inlineCode",{parentName:"p"},"mirai-api-http")," \u7684\u914d\u7f6e\u4fee\u6539 ",(0,o.kt)("inlineCode",{parentName:"p"},"verify_key")," \u548c ",(0,o.kt)("inlineCode",{parentName:"p"},"port")," \u7684\u503c\uff0c\u7136\u540e\u8fd0\u884c\u3002\u5982\u679c\u4f60\u7684\u8bbe\u7f6e\u662f\u6b63\u786e\u7684\uff0c\u7a0b\u5e8f\u4f1a\u8f93\u51fa\u7c7b\u4f3c\u4e8e\u8fd9\u6837\u7684\u5185\u5bb9\uff1a"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre"},"method '__http_verify' has called\nsessionKey: KT26iQBo\nmethod '__http_bind' has called\nmethod '__http_main_loop' starts\n")),(0,o.kt)("p",null,"\u6253\u5f00\u4e00\u4e2a QQ \u7fa4\uff0c\u968f\u4fbf\u53d1\u9001\u4e00\u6761\u6d88\u606f\uff08\u524d\u63d0\u662f\u4f60\u7684 bot \u4e5f\u5728\u8fd9\u4e2a\u7fa4\uff09\uff1b\u6216\u8005\u5411 bot \u79c1\u53d1\u4e00\u6761\u6d88\u606f\uff08\u524d\u63d0\u662f\u4f60\u5df2\u7ecf\u6dfb\u52a0 bot \u4e3a\u597d\u53cb\uff09\u3002\u4e0d\u51fa\u610f\u5916\u7684\u8bdd\uff0c\u4f60\u4f1a\u6536\u5230 bot \u7684\u56de\u590d\uff1a"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre"},"Hello world!\n")),(0,o.kt)("p",null,"\u597d\u7684\uff0c\u73b0\u5728\u53ef\u4ee5\u795d\u8d3a\uff0c\u4f60\u7684 bot \u8fd0\u884c\u6210\u529f\u4e86\uff01"))}m.isMDXComponent=!0}}]);