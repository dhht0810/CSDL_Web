package com.example.thu_vien.service;

import java.util.List;

import com.example.thu_vien.entities.Chap;

public interface ChapService {

    List<Chap> findById_truyen(int id_truyen);

    void save(Chap chap);

    void delete(Integer id);
}
