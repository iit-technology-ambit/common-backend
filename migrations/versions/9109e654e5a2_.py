"""empty message

Revision ID: 9109e654e5a2
Revises: 
Create Date: 2019-07-30 22:16:16.840067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9109e654e5a2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('imgLink',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('link', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=True),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('dob', sa.DateTime(), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('fb_handle', sa.String(length=255), nullable=True),
    sa.Column('g_handle', sa.String(length=255), nullable=True),
    sa.Column('medium_handle', sa.String(length=255), nullable=True),
    sa.Column('twitter_handle', sa.String(length=255), nullable=True),
    sa.Column('linkedin_handle', sa.String(length=255), nullable=True),
    sa.Column('profile_picture', sa.Integer(), nullable=True),
    sa.Column('bio', sa.Text(), nullable=True),
    sa.Column('occupation', sa.String(length=255), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('creation_time', sa.DateTime(), nullable=True),
    sa.Column('is_verified', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('payment',
    sa.Column('pay_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=256), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('api_response', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['username'], ['user.username'], ),
    sa.PrimaryKeyConstraint('pay_id')
    )
    op.create_table('post',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('_author_id', sa.String(length=256), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('post_time', sa.DateTime(), nullable=True),
    sa.Column('avg_rating', sa.Float(), nullable=True),
    sa.Column('num_rating', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['_author_id'], ['user.username'], ),
    sa.PrimaryKeyConstraint('post_id')
    )
    op.create_table('userTagJunction',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('keyword_id', sa.Integer(), nullable=False),
    sa.Column('priority', sa.Enum('less_of_these', 'follow', 'more_of_these', name='prioritytype'), nullable=True),
    sa.ForeignKeyConstraint(['keyword_id'], ['tag.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'keyword_id')
    )
    op.create_table('imgPostJunction',
    sa.Column('img_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['img_id'], ['imgLink.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['post.post_id'], ),
    sa.PrimaryKeyConstraint('img_id')
    )
    op.create_table('postTagJunction',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.post_id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('post_id', 'tag_id')
    )
    op.create_table('userPostInteraction',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('save', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.post_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userPostInteraction')
    op.drop_table('postTagJunction')
    op.drop_table('imgPostJunction')
    op.drop_table('userTagJunction')
    op.drop_table('post')
    op.drop_table('payment')
    op.drop_table('user')
    op.drop_table('tag')
    op.drop_table('imgLink')
    # ### end Alembic commands ###