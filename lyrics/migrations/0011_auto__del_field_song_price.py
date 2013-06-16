# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Song.price'
        db.delete_column(u'lyrics_song', 'price')


    def backwards(self, orm):
        # Adding field 'Song.price'
        db.add_column(u'lyrics_song', 'price',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    models = {
        u'lyrics.album': {
            'Meta': {'object_name': 'Album'},
            'band': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lyrics.Band']"}),
            'genres': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['lyrics.Genre']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_sold': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'release_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'lyrics.artist': {
            'Meta': {'object_name': 'Artist'},
            'date_of_birth': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instrument': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'lyrics.band': {
            'Meta': {'object_name': 'Band'},
            'artists': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['lyrics.Artist']", 'symmetrical': 'False'}),
            'band': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'genre': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['lyrics.Genre']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lyrics.genre': {
            'Meta': {'object_name': 'Genre'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'lyrics.song': {
            'Meta': {'object_name': 'Song'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lyrics.Album']"}),
            'band': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lyrics.Band']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lyrics': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['lyrics']