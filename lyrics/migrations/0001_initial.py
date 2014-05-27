# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Artist'
        db.create_table(u'lyrics_artist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('instrument', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('date_of_birth', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'lyrics', ['Artist'])

        # Adding model 'Genre'
        db.create_table(u'lyrics_genre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('about', self.gf('django.db.models.fields.TextField')()),
            ('created_at', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'lyrics', ['Genre'])

        # Adding model 'Band'
        db.create_table(u'lyrics_band', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('band', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'lyrics', ['Band'])

        # Adding M2M table for field genre on 'Band'
        m2m_table_name = db.shorten_name(u'lyrics_band_genre')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('band', models.ForeignKey(orm[u'lyrics.band'], null=False)),
            ('genre', models.ForeignKey(orm[u'lyrics.genre'], null=False))
        ))
        db.create_unique(m2m_table_name, ['band_id', 'genre_id'])

        # Adding M2M table for field artists on 'Band'
        m2m_table_name = db.shorten_name(u'lyrics_band_artists')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('band', models.ForeignKey(orm[u'lyrics.band'], null=False)),
            ('artist', models.ForeignKey(orm[u'lyrics.artist'], null=False))
        ))
        db.create_unique(m2m_table_name, ['band_id', 'artist_id'])

        # Adding model 'Album'
        db.create_table(u'lyrics_album', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('band', self.gf('django.db.models.fields.related.ForeignKey')(related_name='albums', to=orm['lyrics.Band'])),
            ('release_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('num_sold', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'lyrics', ['Album'])

        # Adding M2M table for field genres on 'Album'
        m2m_table_name = db.shorten_name(u'lyrics_album_genres')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('album', models.ForeignKey(orm[u'lyrics.album'], null=False)),
            ('genre', models.ForeignKey(orm[u'lyrics.genre'], null=False))
        ))
        db.create_unique(m2m_table_name, ['album_id', 'genre_id'])

        # Adding model 'Jargon'
        db.create_table(u'lyrics_jargon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('song_title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('jargon_info', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'lyrics', ['Jargon'])

        # Adding model 'JargonThrough'
        db.create_table(u'lyrics_jargonthrough', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('song', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lyrics.Song'])),
            ('jargon', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lyrics.Jargon'])),
            ('extra_info', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'lyrics', ['JargonThrough'])

        # Adding model 'Song'
        db.create_table(u'lyrics_song', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('lyrics', self.gf('django.db.models.fields.TextField')()),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(related_name='songs', to=orm['lyrics.Album'])),
            ('band', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lyrics.Band'], null=True, blank=True)),
        ))
        db.send_create_signal(u'lyrics', ['Song'])


    def backwards(self, orm):
        # Deleting model 'Artist'
        db.delete_table(u'lyrics_artist')

        # Deleting model 'Genre'
        db.delete_table(u'lyrics_genre')

        # Deleting model 'Band'
        db.delete_table(u'lyrics_band')

        # Removing M2M table for field genre on 'Band'
        db.delete_table(db.shorten_name(u'lyrics_band_genre'))

        # Removing M2M table for field artists on 'Band'
        db.delete_table(db.shorten_name(u'lyrics_band_artists'))

        # Deleting model 'Album'
        db.delete_table(u'lyrics_album')

        # Removing M2M table for field genres on 'Album'
        db.delete_table(db.shorten_name(u'lyrics_album_genres'))

        # Deleting model 'Jargon'
        db.delete_table(u'lyrics_jargon')

        # Deleting model 'JargonThrough'
        db.delete_table(u'lyrics_jargonthrough')

        # Deleting model 'Song'
        db.delete_table(u'lyrics_song')


    models = {
        u'lyrics.album': {
            'Meta': {'object_name': 'Album'},
            'band': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'albums'", 'to': u"orm['lyrics.Band']"}),
            'genres': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'albums'", 'symmetrical': 'False', 'to': u"orm['lyrics.Genre']"}),
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
            'genre': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'bands'", 'symmetrical': 'False', 'to': u"orm['lyrics.Genre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'lyrics.genre': {
            'Meta': {'object_name': 'Genre'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'lyrics.jargon': {
            'Meta': {'object_name': 'Jargon'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jargon_info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'song_title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'lyrics.jargonthrough': {
            'Meta': {'object_name': 'JargonThrough'},
            'extra_info': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jargon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lyrics.Jargon']"}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lyrics.Song']"})
        },
        u'lyrics.song': {
            'Meta': {'object_name': 'Song'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'songs'", 'to': u"orm['lyrics.Album']"}),
            'band': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lyrics.Band']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jargon': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['lyrics.Jargon']", 'null': 'True', 'through': u"orm['lyrics.JargonThrough']", 'blank': 'True'}),
            'lyrics': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['lyrics']