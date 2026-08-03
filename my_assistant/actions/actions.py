# -*- coding: utf-8 -*-
"""
自定义Action实现

在这里定义你的自定义动作逻辑。
每个自定义动作需要继承Action基类并实现run方法。

注意：
- Action 类会在 Agent.load() 时自动发现和注册
- run 方法必须返回 ActionResult 对象
- 使用 result.add_response(text) 添加响应文本
"""

from typing import Any, Text

from atguigu_ai.agent.actions import Action, ActionResult


class ActionGreet(Action):
    """问候动作。"""
    
    @property
    def name(self) -> Text:
        return "action_greet"
    
    async def run(
        self,
        tracker: Any,
        domain: Any,
        **kwargs: Any,
    ) -> ActionResult:
        """执行问候动作。
        
        根据用户是否已知，返回个性化问候。
        """
        result = ActionResult()
        user_name = tracker.get_slot("user_name") if hasattr(tracker, 'get_slot') else None
        if user_name:
            result.add_response(f"你好，{user_name}！有什么可以帮助你的吗？")
        else:
            result.add_response("你好！我是Atguigu AI助手，有什么可以帮助你的吗？")
        return result


class ActionGoodbye(Action):
    """告别动作。"""
    
    @property
    def name(self) -> Text:
        return "action_goodbye"
    
    async def run(
        self,
        tracker: Any,
        domain: Any,
        **kwargs: Any,
    ) -> ActionResult:
        """执行告别动作。"""
        result = ActionResult()
        result.add_response("再见！祝您生活愉快！")
        return result


class ActionHandleHelp(Action):
    """处理帮助请求的动作。"""
    
    @property
    def name(self) -> Text:
        return "action_handle_help"
    
    async def run(
        self,
        tracker: Any,
        domain: Any,
        **kwargs: Any,
    ) -> ActionResult:
        """处理帮助请求。
        
        根据用户最新消息提供相应帮助。
        """
        result = ActionResult()
        latest_message = tracker.latest_message if hasattr(tracker, 'latest_message') else None
        if latest_message:
            text = latest_message.text if hasattr(latest_message, 'text') else ""
            if text:
                result.add_response(f"好的，我来帮您处理关于'{text}'的问题。")
                return result
        result.add_response("请告诉我您需要什么帮助。")
        return result
