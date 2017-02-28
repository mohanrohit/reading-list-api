from end_statement import end

from app import db

class Model(db.Model):
  __abstract__ = True

  def save(self):
    db.session.add(self)
    db.session.commit()
  end
end