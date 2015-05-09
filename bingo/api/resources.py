import psycopg2
import operator
from flask import request, jsonify
from flask.ext.restful import Resource, abort
from flask.ext.restful.reqparse import RequestParser
from flask.ext.stormpath import groups_required

from bingo.api.models import RuleT
from bingo.wsgi import db

def _get_rule(rule):
    return {
        rule.name: {
            'rule': rule.value,
            'active': rule.active,
            'id': rule.id,
        }
    }

class Rules(Resource):
    def get(self):
        rules = map(_get_rule, RuleT.query.all())
        rules.sort()
        response = {'rules': {}}
        for rule in rules:
            response['rules'].update(rule)
        return jsonify(response)

    @groups_required(['admin'])
    def post(self):
        rj = request.get_json(force=True)
        rule = RuleT.query.filter_by(name=rj['name']).first()
        if rule:
            abort(403, message="Rule already exists: {0}".format(rj['name']))
        elif rj:
            r = RuleT(**rj)
            try:
                db.session.add(r)
                db.session.commit()
                return jsonify({"status": "success"})
            except Exception as exc:
                abort(500, message="Unable to create rule: {0}".format(r['name']))
        abort(500, message="Something failed.")

    @groups_required(['admin'])
    def put(self):
        rj = request.get_json(force=True)
        rule = RuleT.query.filter_by(name=rj['name']).first()
        if not rule:
            abort(404, message="Rule not found: {0}".format(name))
        elif rj:
            if 'value' in rj:
                rule.value = rj['value']
            if 'active' in rj:
                rule.active = rj['active']
            try:
                db.session.commit()
                return jsonify({"status": "updated"})
            except Exception as exc:
                abort(500, message="Unable to update rule: {0}".format(r['name']))
        abort(500, message="Something failed.")


class Rule(Resource):
    def get(self, name):
        if name:
            rule = RuleT.query.filter_by(name=name).first()
            return jsonify({'rule': _get_rule(rule)})

    @groups_required(['player'])
    def put(self, name):
        rule = RuleT.query.filter_by(name=name).first()
        if not rule:
            abort(404, message="Rule not found: {0}".format(name))
        if rule.active:
            rule.active = False
        else:
            rule.active = True
        try:
            db.session.commit()
            return jsonify({"status": "updated"})
        except Exception as exc:
            abort(500, message="Unable to update rule: {0}".format(r['name']))
        abort(500, message="Something failed.")

    def delete(self, name):
        rule = RuleT.query.filter_by(name=name).first()
        if not rule:
            abort(404, message="Rule not found: {0}".format(name))
        try:
            db.session.delete(rule)
            db.session.commit()
            return jsonify({'status': 'deleted'})
        except Exception as exc:
            abort(500, message='Somthing failed.')
