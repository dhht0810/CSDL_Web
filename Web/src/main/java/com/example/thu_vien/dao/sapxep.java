package com.example.thu_vien.dao;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.example.thu_vien.entities.Truyen;
import com.example.thu_vien.model.truyen;

import jakarta.persistence.EntityManager;
import jakarta.persistence.Query;

@Repository
public class sapxep {
    @Autowired
    private EntityManager entityManager;

    @SuppressWarnings("unchecked")
    public List<truyen> sap_xep(String name) {
        String sql = "Select new " + truyen.class.getName() + " (ten, tacgia) "
                    + "from " + Truyen.class.getName() + " order by " + name + " desc";
        Query query = entityManager.createQuery(sql,truyen.class);
        return query.getResultList();
    }
}
