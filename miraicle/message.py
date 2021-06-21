import time
import random
from typing import Optional, Union, List

from .display import color


class Plain:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return self.text

    def __eq__(self, other):
        if isinstance(other, Plain):
            return self.text == other.text
        else:
            return False

    def to_json(self):
        return {'type': 'Plain', 'text': self.text}

    @staticmethod
    def from_json(json: dict):
        text = json.get('text', None)
        return Plain(text)


class At:
    def __init__(self, qq, display: str = None):
        self.qq = qq
        self.display = display

    def __repr__(self):
        if self.display:
            return f'[At:{self.qq} | {self.display}]'
        else:
            return f'[At:{self.qq}]'

    def __eq__(self, other):
        if isinstance(other, At):
            return self.qq == other.qq
        else:
            return False

    def to_json(self):
        return {'type': 'At', 'target': self.qq}

    @staticmethod
    def from_json(json: dict):
        qq = json.get('target', None)
        display = json.get('display', None)
        return At(qq, display)


class AtAll:
    def __init__(self):
        pass

    def __repr__(self):
        return '[AtAll]'

    def __eq__(self, other):
        if isinstance(other, AtAll):
            return True
        else:
            return False

    @staticmethod
    def to_json():
        return {'type': 'AtAll'}

    @staticmethod
    def from_json(json: dict):
        return AtAll()


class Face:
    def __init__(self, face_id: int = None, name: str = None):
        self.face_id = face_id
        self.name = name

    def __repr__(self):
        if self.face_id and self.name:
            return f'[Face:{self.face_id} | {self.name}]'
        elif self.face_id:
            return f'[Face:{self.face_id}]'
        else:
            return f'[Face:{self.name}]'

    def __eq__(self, other):
        if isinstance(other, Face):
            return self.face_id == other.face_id if self.face_id and other.face_id else self.name == other.name
        else:
            return False

    def to_json(self):
        if self.face_id:
            return {'type': 'Face', 'faceId': self.face_id}
        else:
            return {'type': 'Face', 'name': self.name}

    @staticmethod
    def from_json(json: dict):
        face_id = json.get('faceId', None)
        name = json.get('name', None)
        return Face(face_id, name)

    @staticmethod
    def from_face_id(face_id: int):
        return Face(face_id=face_id)

    @staticmethod
    def from_name(name: str):
        return Face(name=name)


class Image:
    def __init__(self, path: str = None, url: str = None, image_id: str = None):
        self.path = path
        self.url = url
        self.image_id = image_id

    def __repr__(self):
        if not self.url:
            return f'[Image:{self.image_id}]'
        else:
            return f'[Image:{self.image_id} | {self.url}]'

    def __eq__(self, other):
        if isinstance(other, Image):
            return self.image_id == other.image_id
        else:
            return False

    def to_json(self):
        if self.path:
            return {'type': 'Image', 'path': self.path}
        elif self.url:
            return {'type': 'Image', 'url': self.url}
        elif self.image_id:
            return {'type': 'Image', 'imageId': self.image_id}

    @property
    def is_flash(self) -> bool:
        return False

    def to_flash(self) -> 'FlashImage':
        return FlashImage(path=self.path, url=self.url, image_id=self.image_id)

    def to_normal(self) -> 'Image':
        return self

    @staticmethod
    def from_json(json: dict) -> 'Image':
        path = json.get('path', None)
        url = json.get('url', None)
        image_id = json.get('imageId', None)
        return Image(path, url, image_id)

    @staticmethod
    def from_file(path: str) -> 'Image':
        return Image(path=path)

    @staticmethod
    def from_url(url: str) -> 'Image':
        return Image(url=url)

    @staticmethod
    def from_id(image_id: str) -> 'Image':
        return Image(image_id=image_id)


class FlashImage:
    def __init__(self, path: str = None, url: str = None, image_id: str = None):
        self.path = path
        self.url = url
        self.image_id = image_id

    def __repr__(self):
        if not self.url:
            return f'[Image:{self.image_id}]'
        else:
            return f'[Image:{self.image_id} | {self.url}]'

    def __eq__(self, other):
        if isinstance(other, FlashImage):
            return self.image_id == other.image_id
        else:
            return False

    def to_json(self):
        if self.path:
            return {'type': 'FlashImage', 'path': self.path}
        elif self.url:
            return {'type': 'FlashImage', 'url': self.url}
        elif self.image_id:
            return {'type': 'FlashImage', 'imageId': self.image_id}

    @property
    def is_flash(self) -> bool:
        return True

    def to_normal(self) -> Image:
        return Image(path=self.path, url=self.url, image_id=self.image_id)

    def to_flash(self) -> 'FlashImage':
        return self

    @staticmethod
    def from_json(json: dict) -> 'FlashImage':
        path = json.get('path', None)
        url = json.get('url', None)
        image_id = json.get('imageId', None)
        return FlashImage(path, url, image_id)

    @staticmethod
    def from_file(path: str) -> 'FlashImage':
        return FlashImage(path=path)

    @staticmethod
    def from_url(url: str) -> 'FlashImage':
        return FlashImage(url=url)

    @staticmethod
    def from_id(image_id: str) -> 'FlashImage':
        return FlashImage(image_id=image_id)


class Voice:
    def __init__(self, path: str = None, url: str = None, voice_id: str = None):
        self.path = path
        self.url = url
        self.voice_id = voice_id

    def __repr__(self):
        if not self.url:
            return f'[Voice:{self.voice_id}]'
        else:
            return f'[Voice:{self.voice_id} | {self.url}]'

    def __eq__(self, other):
        if isinstance(other, Voice):
            return self.voice_id == other.voice_id
        else:
            return False

    def to_json(self):
        if self.path:
            return {'type': 'Voice', 'path': self.path}
        elif self.url:
            return {'type': 'Voice', 'url': self.url}
        elif self.voice_id:
            return {'type': 'Voice', 'voiceId': self.voice_id}

    @staticmethod
    def from_json(json: dict) -> 'Voice':
        path = json.get('path', None)
        url = json.get('url', None)
        voice_id = json.get('voiceId', None)
        return Voice(path, url, voice_id)

    @staticmethod
    def from_file(path: str) -> 'Voice':
        return Voice(path=path)

    @staticmethod
    def from_url(url: str) -> 'Voice':
        return Voice(url=url)

    @staticmethod
    def from_id(voice_id: str) -> 'Voice':
        return Voice(voice_id=voice_id)


class Xml:
    def __init__(self, xml):
        self.xml = xml

    def __repr__(self):
        return f'[Xml:{self.xml}]'

    def __eq__(self, other):
        if isinstance(other, Xml):
            return self.xml == other.xml
        else:
            return False

    def to_json(self):
        return {'type': 'Xml', 'xml': self.xml}

    @staticmethod
    def from_json(json: dict):
        xml = json.get('xml', None)
        return Xml(xml=xml)


class Json:
    def __init__(self, json):
        self.json = json

    def __repr__(self):
        return f'[Json:{self.json}]'

    def __eq__(self, other):
        if isinstance(other, Json):
            return self.json == other.json
        else:
            return False

    def to_json(self):
        return {'type': 'Json', 'json': self.json}

    @staticmethod
    def from_json(json: dict):
        json = json.get('json', None)
        return Json(json=json)


class App:
    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return f'[App:{self.content}]'

    def __eq__(self, other):
        if isinstance(other, App):
            return self.content == other.content
        else:
            return False

    def to_json(self):
        return {'type': 'App', 'content': self.content}

    @staticmethod
    def from_json(json: dict):
        json = json.get('content', None)
        return App(content=json)


class Dice:
    def __init__(self, value: Optional[int] = None):
        self.value = value if value else random.randint(1, 6)

    def __repr__(self):
        return f'[Dice:{self.value}]'

    def __eq__(self, other):
        if isinstance(other, Dice):
            return self.value == other.value
        else:
            return False

    def to_json(self):
        return {'type': 'Dice', 'value': self.value}

    @staticmethod
    def from_json(json: dict):
        value = json.get('value', None)
        return Dice(value=value)


class File:
    def __init__(self, file_id: str, internal_id: int, name: str, size: int):
        self.file_id = file_id
        self.internal_id = internal_id
        self.name = name
        self.size = size

    def __repr__(self):
        return f'[File:{self.name} | {self.file_id}]'

    @staticmethod
    def from_json(json: dict):
        file_id = json.get('id', None)
        internal_id = json.get('internalId', None)
        name = json.get('name', None)
        size = json.get('size', None)
        return File(file_id=file_id, internal_id=internal_id, name=name, size=size)


class Message:
    def __init__(self, msg: dict):
        self.json = msg
        msg_chain = msg.get('messageChain', None)
        try:
            self.id = msg_chain[0].get('id', None)
        except:
            self.id = None
        try:
            self.time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(msg_chain[0].get('time', 0)))
        except:
            self.time = None

        try:
            chain = []
            text = ''
            for ele in msg_chain[1:]:
                if ele['type'] in ['Plain', 'At', 'AtAll', 'Face', 'Image', 'FlashImage',
                                   'Voice', 'Xml', 'Json', 'App', 'Dice', 'File']:
                    instance = eval(ele['type']).from_json(ele)
                    chain.append(instance)
                    text += instance.__repr__()
                else:
                    text += f"[{ele['type']}]"
            self.chain = chain
            self.text = text
        except:
            self.chain = []
            self.text = ''

    def __eq__(self, other):
        return True if self.chain == other.chain else False

    @property
    def plain(self) -> str:
        text = ''
        for ele in self.chain:
            if type(ele) == Plain:
                text += ele.text
        return text

    @property
    def first_image(self) -> Optional[Union[Image, FlashImage]]:
        for ele in self.chain:
            if type(ele) in [Image, FlashImage]:
                return ele
        return None

    @property
    def images(self) -> List[Union[Image, FlashImage]]:
        return [ele for ele in self.chain if type(ele) in [Image, FlashImage]]

    @property
    def file(self) -> Optional[File]:
        for ele in self.chain:
            if isinstance(ele, File):
                return ele
        return None


class GroupMessage(Message):
    def __init__(self, msg: dict):
        super().__init__(msg)
        sender = msg.get('sender', {})
        self.sender = sender.get('id', None)
        self.sender_name = sender.get('memberName', None)
        group = sender.get('group', {})
        self.group = group.get('id', None)
        self.group_name = group.get('name', None)

    def __repr__(self):
        return f'{self.time} GroupMessage #{self.id} {self.group_name}({self.group})' \
               f' - {self.sender_name}({self.sender}): {self.text.__repr__()}'


class FriendMessage(Message):
    def __init__(self, msg: dict):
        super().__init__(msg)
        sender = msg.get('sender', {})
        self.sender = sender.get('id', None)
        self.sender_name = sender.get('nickname', None)

    def __repr__(self):
        return f'{self.time} FriendMessage #{self.id}' \
               f' - {self.sender_name}({self.sender}): {self.text.__repr__()}'


class TempMessage(Message):
    def __init__(self, msg: dict):
        super().__init__(msg)
        sender = msg.get('sender', {})
        self.sender = sender.get('id', None)
        self.sender_name = sender.get('memberName', None)
        group = sender.get('group', {})
        self.group = group.get('id', None)
        self.group_name = group.get('name', None)

    def __repr__(self):
        return f'{self.time} TempMessage #{self.id} {self.group_name}({self.group})' \
               f' - {self.sender_name}({self.sender}): {self.text.__repr__()}'


class GroupRecallEvent:
    def __init__(self, msg: dict):
        self.json = msg
        self.id = msg.get('messageId', None)
        self.author = msg.get('authorId', None)
        group = msg.get('group', {})
        self.group = group.get('id', None)
        self.group_name = group.get('name', None)
        operator = msg.get('operator', {})
        self.operator = operator.get('id', None)
        self.operator_name = operator.get('memberName', None)
        self.operator_permission = operator.get('permission', None)

    def __repr__(self):
        return f'GroupRecallEvent #{self.id} {self.group_name}({self.group})' \
               f' - {self.operator_name}({self.operator}) recalled a message from {self.author}'


class MemberCardChangeEvent:
    def __init__(self, msg: dict):
        self.json = msg
        self.origin = msg.get('origin', None)
        self.current = msg.get('current', None)
        member = msg.get('member', {})
        self.member = member.get('id', None)
        self.member_name = member.get('memberName', None)
        group = member.get('group', {})
        self.group = group.get('id', None)
        self.group_name = group.get('name', None)
        operator = msg.get('operator', {})
        if operator is None:
            operator = {}
        self.operator = operator.get('id')
        self.operator_name = operator.get('memberName', None)
        self.operator_permission = operator.get('permission', None)

    def __repr__(self):
        return f"MemberCardChangeEvent {self.group_name}({self.group})" \
               f" - {self.member_name}({self.member})'s card was changed from '{self.origin}' to '{self.current}'" \
               f" by {self.operator_name}({self.operator})"


class BotOnlineEvent:
    def __init__(self, msg: dict):
        self.json = msg
        self.type = msg.get('type', None)

    def __repr__(self):
        return color(self.type, 'green')


class BotOfflineEvent:
    def __init__(self, msg: dict):
        self.json = msg
        self.type = msg.get('type', None)

    def __repr__(self):
        return color(self.type, 'red')
