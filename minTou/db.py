#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  @author: WuBingBing

import pymysql
import re
import gVariable


class DB:

    def query(self, sql):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='mtbill')
        cur = conn.cursor()
        cur.execute(sql)
        for r in cur.fetchall():
            return r
            cur.close()
        conn.close()

    def get_code(self):
        code = self.query(
            "SELECT smsParam FROM sms_record "
            "WHERE smsParam like '%code%' AND receiveMobiles = "
            + gVariable.GVariable.teleNum +
            " ORDER BY id DESC LIMIT 1"
            )
        return str((re.compile(r'\d+').findall(str(code))))
