from __future__ import annotations

from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from typing import Optional
from sqlalchemy import DateTime, func, Boolean, Text

import asyncio
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime, func, Boolean, Text


class Base(AsyncAttrs, DeclarativeBase):
    pass

class Summary(Base): 
    __tablename__ = "videos_summary"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[Optional[str]] 
    summary_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True) 
    gpt_information: Mapped[Optional[str]] = mapped_column(Text, nullable=True) 
    gpt_model_name: Mapped[Optional[str]]
    gpt_input_token_count: Mapped[Optional[str]]
    gpt_output_token_count: Mapped[Optional[str]]

    summary_path: Mapped[Optional[str]] 
    summary_start_date: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True)
    summary_end_date: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True)
    summary_time: Mapped[Optional[int]] 
    summary_token_count: Mapped[Optional[int]]
    summary_word_count: Mapped[Optional[int]]
    summary_char_count: Mapped[Optional[int]]
    created_at: Mapped[Optional[DateTime]] = mapped_column(DateTime, default=func.now(), nullable=False)
    updated_at: Mapped[Optional[DateTime]] = mapped_column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    video_id: Mapped[int] = mapped_column(ForeignKey("videos_video.id"))
    video: Mapped["Video"] = relationship(back_populates="summaries")

    def __repr__(self) -> str:
        return f"Summary(id={self.id!r}, title={self.title!r}, summary={self.summary_text[10]!r})"
    
class Video(Base): 
    __tablename__ = "videos_video"
    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str]
    title: Mapped[Optional[str]]    
    ext: Mapped[Optional[str]]
    title_with_ext: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    channel_name: Mapped[Optional[str]]
    channel_url: Mapped[Optional[str]]
    upload_date_youtube: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True)
    duration: Mapped[Optional[int]]
    view_count: Mapped[Optional[int]]
    like_count: Mapped[Optional[int]]
    categories: Mapped[Optional[str]] 
    tags: Mapped[Optional[str]]

    audio_path: Mapped[Optional[str]]
    subtitles: Mapped[Optional[str]] = mapped_column(Text, nullable=True) # long string
    transcript: Mapped[Optional[str]] = mapped_column(Text, nullable=True)  # can hold arbitrarily long string
    transcript_path: Mapped[Optional[str]] 
    transcribing_start_date: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True)
    transcribing_end_date: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True)
    transcribing_time: Mapped[Optional[int]]
    transcript_from: Mapped[Optional[str]]
    transcript_word_count: Mapped[Optional[int]]
    transcript_token_count: Mapped[Optional[int]]
    transcript_character_count: Mapped[Optional[int]]

    date_uploaded: Mapped[Optional[DateTime]] =  mapped_column(DateTime, nullable=True)
    download_start_datetime: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True)
    download_end_datetime: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True)
    download_time: Mapped[Optional[int]]
    created_at: Mapped[Optional[DateTime]] = mapped_column(DateTime, default=func.now(), nullable=False)
    updated_at: Mapped[Optional[DateTime]] = mapped_column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    is_summarized: Mapped[Optional[Boolean]] = mapped_column(Boolean, default=False)
    is_transcribed: Mapped[Optional[Boolean]] = mapped_column(Boolean, default=False)
    status : Mapped[Optional[str]] = mapped_column(default="Pending.") # Pending / Done 
    
    playlist_id: Mapped[Optional[str]]
    playlist_order: Mapped[Optional[int]]
    is_in_playlist: Mapped[Optional[Boolean]]= mapped_column(Boolean, default=False)

    summaries: Mapped[List["Summary"]] = relationship(back_populates="video", cascade="all, delete-orphan", lazy='select')

    def __repr__(self) -> str:
        return f"Video(id={self.id!r}, url={self.url!r}, title={self.title!r})"

class B(Base):
    __tablename__ = "b"
    id: Mapped[int] = mapped_column(primary_key=True)
    a_id: Mapped[int] = mapped_column(ForeignKey("a.id"))
    data: Mapped[str]

class A(Base):
    __tablename__ = "a"
    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[str]
    create_date: Mapped[Optional[DateTime]] = mapped_column(DateTime, default=func.now(), nullable=False)
    bs: Mapped[List[B]] = relationship()
