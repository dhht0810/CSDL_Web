package com.example.thu_vien.dao;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.example.thu_vien.entities.Chap;
import com.example.thu_vien.entities.The_loai;
import com.example.thu_vien.entities.Truyen;
import com.example.thu_vien.entities.xd_the_loai;
import com.example.thu_vien.model.*;

import jakarta.persistence.EntityManager;
import jakarta.persistence.Query;

@Repository
public class DAO {
    @Autowired
    private EntityManager entityManager;

    @SuppressWarnings("unchecked")
    public List<truyen> find(int id) {
        String sql = "Select new " + truyen.class.getName() + " (a.id, a.ten, tacgia, c.filePath)"
                    + " from xd_the_loai b join " + Truyen.class.getName() + " a on a.id = b.id_truyen "
                    + "join " + Chap.class.getName() + " c on a.id = c.idtr where c.id_chap = 0 and id_the_loai = " + String.valueOf(id);
        Query query = entityManager.createQuery(sql, truyen.class);
        return query.getResultList();
    }

    @SuppressWarnings("unchecked")
    public List<xd_the_loai> xdtheloai(int id) {
        String sql = "Select (a.id, a.ten) " + "from " 
                    + xd_the_loai.class.getName() + " a  where id_truyen = " + String.valueOf(id);
        Query query = entityManager.createQuery(sql,truyen.class);
        return query.getResultList();
    }

    @SuppressWarnings("unchecked")
    public List<Chap> showChaps(int id_truyen) {
        String sql = "Select new " + chap.class.getName() + " (id, idtr, filePath, id_chap) from " + Chap.class.getName() + " where id_truyen = " + String.valueOf(id_truyen);
        Query query = entityManager.createQuery(sql);
        return query.getResultList();
    }

    
}
